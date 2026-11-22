#!/usr/bin/env python3
"""Buat narasi.wav (gabungan) dan kata.json (waktu tiap kata) dari potongan P01.wav, P02.wav, ...
Pakai:
  python3 engine/kata.py <folder-berisi-P*.wav> [--gap 0.5] [--model small]
    -> menulis narasi.wav dan kata.json di folder itu
  python3 engine/kata.py <satu-file.wav>
    -> hanya kata.json di sebelah file itu
Waktu kata dihitung kumulatif: paragraf berikutnya mulai setelah paragraf sebelumnya + jeda,
jadi detik tidak ter-reset per paragraf. Tiap kata juga dicatat paragraf asalnya ("p").
Butuh: pip install faster-whisper, dan ffmpeg/ffprobe terpasang."""
import sys, os, glob, json, subprocess, wave, contextlib
from faster_whisper import WhisperModel

def arg(name, default):
    return sys.argv[sys.argv.index(name)+1] if name in sys.argv else default

src = sys.argv[1]
gap = float(arg('--gap', 0.5))
model = WhisperModel(arg('--model', 'small'), compute_type='int8')

def dur(path):
    out = subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration',
                                   '-of','default=nw=1:nk=1', path])
    return float(out)

def load_audio(path):
    # Decode via ffmpeg langsung (tidak lewat PyAV, yang sering bentrok versi): 16 kHz mono float32
    import numpy as np
    raw = subprocess.check_output(['ffmpeg','-v','error','-i',path,'-f','f32le','-ac','1','-ar','16000','-'])
    return np.frombuffer(raw, dtype=np.float32)

def words_of(path):
    segs, _ = model.transcribe(load_audio(path), language='id', word_timestamps=True)
    return [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]

if os.path.isdir(src):
    files = sorted(glob.glob(os.path.join(src, 'P[0-9][0-9].wav')))
    if not files: sys.exit('Tidak ada P01.wav dst. di folder itu')
    offset, words = 0.0, []
    for i, f in enumerate(files, 1):
        for w, s, e in words_of(f):
            words.append({'w': w, 's': round(offset+s,3), 'e': round(offset+e,3), 'p': i})
        offset += dur(f) + gap
        print(os.path.basename(f), 'selesai, total sampai', round(offset,2), 'dtk')
    # gabung wav dengan jeda hening
    lst = os.path.join(src, '_concat.txt')
    sil = os.path.join(src, '_gap.wav')
    ref = files[0]
    subprocess.run(['ffmpeg','-y','-v','error','-f','lavfi','-i',f'anullsrc=r=44100:cl=mono','-t',str(gap),sil],check=True)
    with open(lst,'w') as fh:
        for i, f in enumerate(files):
            fh.write(f"file '{os.path.abspath(f)}'\n")
            if i < len(files)-1: fh.write(f"file '{os.path.abspath(sil)}'\n")
    out = os.path.join(src,'narasi.wav')
    subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',lst,
                    '-ar','44100','-ac','1',out],check=True)
    os.remove(lst); os.remove(sil)
    jf = os.path.join(src,'kata.json')
else:
    words = [{'w':w,'s':round(s,3),'e':round(e,3),'p':1} for w,s,e in words_of(src)]
    jf = os.path.join(os.path.dirname(os.path.abspath(src)),'kata.json')

json.dump(words, open(jf,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(words),'kata ->',jf)
