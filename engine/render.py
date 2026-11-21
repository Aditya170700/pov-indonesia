#!/usr/bin/env python3
"""Render adegan HTML (window.renderFrame(t)) jadi MP4 lewat Chrome headless + ffmpeg.

Contoh:
  python3 engine/render.py engine/contoh.html out/contoh-10s.mp4 --w 1280 --fps 30
Opsi --audio narasi.wav untuk menambahkan suara; --frames 'detik,detik' untuk simpan PNG cek cepat.
"""
import argparse, base64, os, subprocess, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument('scene'); ap.add_argument('out')
ap.add_argument('--w', type=int, default=1280)
ap.add_argument('--fps', type=int, default=30)
ap.add_argument('--audio')
ap.add_argument('--frames', help='daftar detik untuk disimpan sebagai PNG, mis. 1.5,3.5')
ap.add_argument('--framedir', default='/tmp/frames')
a = ap.parse_args()

scene = Path(a.scene).resolve()
Path(a.out).parent.mkdir(parents=True, exist_ok=True)
cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-vcodec', 'png', '-framerate', str(a.fps), '-i', '-']
if a.audio:
    cmd += ['-i', a.audio]
cmd += ['-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'veryfast', '-crf', '18']
if a.audio:
    cmd += ['-c:a', 'aac', '-b:a', '192k', '-shortest']
cmd += [a.out]

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox', '--disable-gpu'])
    pg = b.new_page(viewport={'width': a.w, 'height': round(a.w * 9 / 16)})
    pg.goto(f'file://{scene}?w={a.w}')
    pg.evaluate('window.ready')
    dur = pg.evaluate('window.DURATION')
    n = int(round(dur * a.fps))
    keep = {round(float(x) * a.fps) for x in a.frames.split(',')} if a.frames else set()
    if keep:
        os.makedirs(a.framedir, exist_ok=True)
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n):
        t = i / a.fps
        png = base64.b64decode(pg.evaluate(f'(()=>{{renderFrame({t});return document.getElementById("c").toDataURL("image/png").split(",")[1];}})()'))
        ff.stdin.write(png)
        if i in keep:
            Path(a.framedir, f'f_{t:05.2f}.png').write_bytes(png)
    ff.stdin.close(); ff.wait()
    b.close()
print(f'selesai: {a.out} ({n} frame, {dur}s)')
