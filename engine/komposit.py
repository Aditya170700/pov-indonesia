#!/usr/bin/env python3
"""Gabungkan base.mp4 + overlay (subtitle & kartu, dari engine/overlay.html) + narasi jadi video akhir.
Pakai: python3 engine/komposit.py videos/001-bebas-korupsi out/001.mp4 [--start 0 --dur 20]
Tanpa --start/--dur = seluruh video. Butuh: base.mp4 (rakit.py), narasi.mp3, kata.json, overlay.json."""
import argparse, base64, json, re, subprocess, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument('dir'); ap.add_argument('out')
ap.add_argument('--start', type=float, default=0); ap.add_argument('--dur', type=float)
ap.add_argument('--fps', type=int, default=30)
ap.add_argument('--frames', help='detik untuk disimpan sebagai PNG cek')
ap.add_argument('--framedir', default='/tmp/frames')
a = ap.parse_args()
d = Path(a.dir); here = Path(__file__).parent
tl = json.load(open(d / 'timeline.json')); total = tl['akhir']
dur = a.dur if a.dur else total - a.start

# --- narasi dinormalkan sekali (-16 LUFS) supaya pratinjau dan render penuh sama keras
norm = d / 'narasi-norm.wav'
if not norm.exists():
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', str(d / 'narasi.mp3'), '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11',
                    '-ar', '44100', '-ac', '1', str(norm)], check=True)

# --- subtitle: koreksi ejaan hasil Whisper agar sama dengan naskah, lalu kelompokkan <=6 kata
FIX = {'gak': 'nggak', 'satupun': 'satu pun', 'diglembungkan': 'digelembungkan', 'diindeks': 'di indeks',
       'kesana': 'ke sana', 'sekalanya': 'skalanya'}
raw = json.load(open(d / 'kata.json')); toks = []
for w in raw:
    t = w['w']; s, e = w['s'], w['e']
    if toks and (t.startswith(',') or t.startswith('-')):           # ',9' '-rata' '-benar' ',78'
        toks[-1]['t'] += t; toks[-1]['e'] = e; continue
    if toks and toks[-1]['t'].lower() == 'di' and t.lower().startswith('sensor'):   # 'di sensor,' -> 'disensor,'
        toks[-1]['t'] = 'di' + t; toks[-1]['e'] = e; continue
    toks.append({'t': t, 's': s, 'e': e})
for k in toks:
    m = re.match(r'^(.*?)([,.?!]*)$', k['t']); core, punct = m.group(1), m.group(2)
    if core.lower() in FIX:
        new = FIX[core.lower()]
        if core[:1].isupper(): new = new[:1].upper() + new[1:]
        k['t'] = new + punct
chunks, cur = [], []
def flush():
    global cur
    if cur: chunks.append({'s': cur[0]['s'], 'e': cur[-1]['e'], 'w': cur}); cur = []
for i, k in enumerate(toks):
    if cur and k['s'] - cur[-1]['e'] > 0.6: flush()
    cur.append(k)
    nxt_end = i + 1 < len(toks) and re.search(r'[.?!]$', toks[i + 1]['t'])
    if (len(cur) >= 6 and not (nxt_end and len(cur) < 7)) or (re.search(r'[.?!]$', k['t']) and len(cur) >= 2) or (k['t'].endswith(',') and len(cur) >= 4): flush()
flush()
for i, c in enumerate(chunks):
    nxt = chunks[i + 1]['s'] if i + 1 < len(chunks) else total
    c['hold'] = max(0.0, min(0.25, nxt - c['e'] - 0.02))
cards = json.load(open(d / 'overlay.json'))['cards']
data = {'duration': total, 'chunks': chunks, 'cards': cards}

n = round(dur * a.fps)
cmd = ['ffmpeg', '-y', '-v', 'error', '-ss', str(a.start), '-t', str(dur), '-i', str(d / 'base.mp4'),
       '-f', 'image2pipe', '-vcodec', 'png', '-framerate', str(a.fps), '-i', '-',
       '-ss', str(a.start), '-i', str(norm),
       '-filter_complex', '[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v];[2:a]apad[a]',
       '-map', '[v]', '-map', '[a]', '-t', str(dur), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
       '-c:a', 'aac', '-b:a', '192k', a.out]
Path(a.out).parent.mkdir(parents=True, exist_ok=True)
keep = {round(float(x) * a.fps) for x in a.frames.split(',')} if a.frames else set()
if keep: Path(a.framedir).mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox', '--disable-gpu'])
    pg = b.new_page(viewport={'width': 1920, 'height': 1080})
    pg.add_init_script('window.DATA=' + json.dumps(data, ensure_ascii=False))
    pg.goto('file://' + str((here / 'overlay.html').resolve()))
    pg.evaluate('window.ready')
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n):
        t = a.start + i / a.fps
        png = base64.b64decode(pg.evaluate(f'(()=>{{renderFrame({t});return document.getElementById("c").toDataURL("image/png").split(",")[1];}})()'))
        ff.stdin.write(png)
        if (round(t * a.fps)) in keep: Path(a.framedir, f'o_{t:06.2f}.png').write_bytes(png)
    ff.stdin.close(); ff.wait(); b.close()
print('selesai:', a.out, n, 'frame')
