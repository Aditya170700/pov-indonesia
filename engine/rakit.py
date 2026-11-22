#!/usr/bin/env python3
"""Rakit klip jadi satu video dasar (tanpa suara) mengikuti timeline.json.
Pakai: python3 engine/rakit.py videos/testing [out.mp4]
Tiap klip: dipercepat/diperlambat (0,9x-1,15x) agar pas dengan jendelanya, sisanya dipotong
atau diam di frame terakhir. Hasil 1920x1080, 30 fps, tanpa audio (audio klip dibuang).
Klip boleh dipakai ulang di beberapa entri timeline. Field opsional per entri:
  "ss": detik awal pemotongan di klip sumber (default 0)
  "zoom": punch-in >1 (mis. 1.35), "cx"/"cy": pusat crop 0-1 (default 0.5)"""
import json, subprocess, sys
from pathlib import Path

d = Path(sys.argv[1]); out = sys.argv[2] if len(sys.argv) > 2 else str(d / 'base.mp4')
tl = json.load(open(d / 'timeline.json')); fps = tl['fps']
ks = tl['klip']
bound = [round(k['mulai'] * fps) for k in ks] + [round(tl['akhir'] * fps)]

def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                          '-of', 'default=nw=1:nk=1', str(p)]))

cmd = ['ffmpeg', '-y', '-v', 'error']; parts = []
for i, k in enumerate(ks):
    p = d / 'klip' / f"{k['k']}.mp4"; cmd += ['-i', str(p)]
    n = bound[i + 1] - bound[i]; win = n / fps; ss = k.get('ss', 0.0); nat = max(dur(p) - ss, 0.5)
    s = min(max(nat / win, 0.9), 1.15)
    played = nat / s
    pad = max(0.0, win - played)
    z = k.get('zoom', 1.0); cx = k.get('cx', 0.5); cy = k.get('cy', 0.5)
    f = f"[{i}:v]"
    if ss > 0: f += f"trim=start={ss:.3f},setpts=PTS-STARTPTS,"
    f += f"setpts=PTS/{s:.5f},fps={fps}"
    if z > 1.0: f += f",crop=iw/{z}:ih/{z}:(iw-iw/{z})*{cx}:(ih-ih/{z})*{cy}"
    f += ",scale=1920:1080:flags=lanczos,setsar=1"
    if pad > 0: f += f",tpad=stop_mode=clone:stop_duration={pad:.3f}"
    f += f",trim=end_frame={n},setpts=PTS-STARTPTS[v{i}]"
    parts.append(f)
    print(f"{k['k']}{'*' if (ss or z>1) else ''}: jendela {win:5.2f}s klip {nat:5.2f}s kecepatan {s:.3f}x " + (f"diam {pad:.2f}s" if pad > 0 else f"potong {played-win:.2f}s"))
fc = ';'.join(parts) + ';' + ''.join(f'[v{i}]' for i in range(len(ks))) + f'concat=n={len(ks)}:v=1:a=0[v]'
cmd += ['-filter_complex', fc, '-map', '[v]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', out]
subprocess.run(cmd, check=True)
print('selesai:', out, round(dur(out), 2), 'dtk')
