# PANDUAN (untuk pemilik repo)

Langkah praktis tiap video. Bagian "Claude" dikerjakan di chat; sisanya di laptop produksi.

## 1. Klip di Google Flow
1. Buka `flow-prompts.md`. Uji **K01** dulu di **360p** dengan `assets/wowo-ref.png` sebagai gambar referensi.
2. Kalau Wowo sudah sesuai, generate K02-K16 dengan cara yang sama (salin prompt, lampirkan gambar referensi). Boleh dibagi ke beberapa akun.
3. Upscale tiap klip ke 720p lewat fitur "tingkatkan resolusi" Flow, lalu unduh. Beri nama `K01.mp4` dst.

## 2. Narasi di VoiceStudio
1. Buka `narasi-bersih.md`. Tempel tiap paragraf (tanpa penanda `P01`) ke fitur **Cerita**, satu baris per paragraf. Suara: clone VoxCPM2. Format: MP3.
2. Isi judul dengan nama video, lalu jalankan. Proses lambat (sekitar 1 jam untuk 2 menit audio), jangan ditutup.
3. Hasil tidak muncul di tab Proyek; file-nya ada di `~/.omnivoice/outputs/story_<kode>.mp3` (cari dengan `ls -t ~/.omnivoice/outputs/*.mp3 | head`). Salin dan ganti nama jadi `narasi.mp3`.
4. Dengarkan sampai habis; catat salah ucap beserta menit:detiknya.

## 3. Timing kata (di laptop)
```
python3 -m venv venv && source venv/bin/activate
pip install faster-whisper          # sekali saja
python3 engine/kata.py narasi.mp3   # hasil: kata.json di folder yang sama
```
Butuh `ffmpeg` terpasang. Pertama kali jalan, model Whisper diunduh dulu.

## 4. Kirim ke Claude
`K01.mp4`-`K16.mp4`, `narasi.mp3`, `kata.json`. Claude merakit (`timeline.json`, `overlay.json`, `rakit.py`, `komposit.py`), memberi pratinjau 20 detik, lalu render penuh.
