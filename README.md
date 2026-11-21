# pov-indonesia

Dapur produksi video simulasi POV bertema politik dan tata kelola Indonesia.

- `CHANNEL.md` — identitas channel, aturan konten, alur produksi
- `STYLE.md` — aturan visual dan audio
- `LOG.md` — daftar video
- `templates/` — template naskah
- `videos/_template/` — salin untuk setiap video baru
- `remotion/` — project Remotion (maskot, subtitle, komponen grafis, thumbnail)
- `assets/` — suara referensi, musik, SFX

## Alat di laptop produksi
- VoiceStudio + VoxCPM2 (narasi), faster-whisper (timing kata)
- Node.js + Remotion (render video)

File besar (narasi `.wav` per video, hasil render `.mp4`) tidak disimpan di git.
