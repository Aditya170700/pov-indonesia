# pov-indonesia

Dapur produksi video simulasi POV bertema politik dan tata kelola Indonesia.

- `CHANNEL.md` — identitas channel, aturan konten, alur produksi
- `STYLE.md` — aturan visual dan audio
- `LOG.md` — daftar video
- `templates/` — template naskah
- `videos/_template/` — salin untuk setiap video baru
- `engine/` — rig Wowo (`wowo.js`), adegan HTML, dan perender ke MP4 (`render.py`)
- `assets/` — suara referensi, musik, SFX

## Alat di laptop produksi
- VoiceStudio + VoxCPM2 (narasi), faster-whisper (timing kata)
- Google Flow (klip adegan), render dan perakitan dilakukan Claude di workspace-nya (Chrome headless + ffmpeg)

File besar (narasi `.wav` per video, hasil render `.mp4`) tidak disimpan di git.
