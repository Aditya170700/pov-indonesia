# pov-indonesia

Dapur produksi video simulasi POV bertema politik dan tata kelola Indonesia.

- `CHANNEL.md` — identitas channel, aturan konten, alur produksi
- `STYLE.md` — aturan visual dan audio
- `LOG.md` — daftar video
- `templates/` — template naskah
- `videos/_template/` — salin untuk setiap video baru
- `engine/` — `rakit.py` (rakit klip), `komposit.py` + `overlay.html` (subtitle, kartu angka, audio), `kata.py` (timing kata, jalan di laptop), rig Wowo (`wowo.js`) dan `render.py` untuk adegan kode
- `PANDUAN.md` — langkah praktis untuk pemilik repo (Flow, VoiceStudio, kata.py)
- `assets/` — suara referensi, musik, SFX

## Alat di laptop produksi
- VoiceStudio (fitur Cerita) + VoxCPM2 clone (narasi), faster-whisper + ffmpeg (timing kata via `engine/kata.py`)
- Google Flow (klip adegan), render dan perakitan dilakukan Claude di workspace-nya (Chrome headless + ffmpeg)

File besar (narasi `.mp3`/`.wav`, klip dan hasil render `.mp4`) tidak disimpan di git.
