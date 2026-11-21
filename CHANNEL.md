# CHANNEL

> Status: nama channel, tagline, dan maskot sudah diputuskan.

## Identitas
- **Nama channel:** POV Endonesa
- **Tagline:** "Coba bayangin kalau Indonesia..."
- **Maskot:** Wowo (stickman fiktif bertopi merah; lihat `STYLE.md`). Wowo = mewakili penonton ("kamu"), bukan tokoh nyata. Sindiran ke pejabat lewat karakter fiktif terpisah (mis. Pak Pejabat), bukan lewat Wowo.
- **Konsep:** video simulasi POV "coba bayangin kalau..." tentang politik dan tata kelola Indonesia. Penonton adalah tokoh utamanya ("kamu").
- **Target penonton:** warga Indonesia usia 18–35 yang resah dengan kondisi politik, menonton sambil santai atau sebelum tidur.
- **Platform:** YouTube (utama), Facebook, TikTok.

## Format
- **Video panjang:** 10–13 menit, 16:9, 1920×1080, 30 fps.
- **Potongan pendek:** 45–60 detik, 9:16, diambil dari bagian terbaik video panjang.
- **Pola judul:** `POV: <skenario>, Ini yang Terjadi`
  - Contoh: `POV: Indonesia Bebas dari Korupsi, Ini yang Terjadi`
  - Contoh: `POV: Pejabat di Indonesia Diisi Orang yang Tepat, Ini yang Terjadi`

## Narator
- Laki-laki, suara hasil clone dari `assets/suara-referensi.wav` (engine VoxCPM2, lisensi Apache-2.0).
- Gaya: santai, tulus, sedikit resah tapi tetap berharap. Seperti teman yang cerita, bukan pembaca berita.

## Gaya bahasa
- Menyapa penonton dengan "kamu".
- Kalimat pendek, mudah diucapkan, tidak akademis.
- Boleh bercanda ringan; tidak memakai makian.
- Angka di naskah ditulis seperti diucapkan (contoh: "dua ribu dua puluh enam", "tiga ratus triliun") supaya TTS tidak salah baca.

## Aturan konten (wajib)
1. Setiap fakta dan angka harus punya sumber kredibel di `riset.md` (contoh: KPK, ICW, BPS, Transparency International, putusan pengadilan, media arus utama).
2. Bagian skenario/hipotesis harus jelas berbeda dari fakta ("bayangin kalau..." vs "faktanya...").
3. Kritik diarahkan ke sistem dan kebijakan. Jangan menuduh orang tertentu tanpa putusan pengadilan atau sumber kredibel.
4. Tidak memihak atau menyerang partai/kandidat tertentu. Tidak menyinggung SARA.
5. Angka di layar harus sama dengan angka di narasi.
6. Saat upload, aktifkan label konten AI (audio/visual sintetis).

## Alur produksi per video
Pembagian kerja: Claude = riset, naskah, storyboard, prompt klip, grafis dan perakitan (render di workspace Claude). Pemilik repo = rekam narasi (VoiceStudio) dan generate klip di Flow.

| # | Tahap | Hasil di `videos/NNN-slug/` | Siapa |
|---|---|---|---|
| 1 | Ide + judul | judul di `naskah.md` | Claude |
| 2 | Riset fakta | `riset.md` | Claude |
| 3 | Naskah (minta persetujuan) | `naskah.md` | Claude + user |
| 4 | Storyboard + peta narasi ke klip | `storyboard.md`, `adegan.json` | Claude |
| 5 | Prompt klip Flow | `flow-prompts.md` | Claude |
| 6 | Uji 1 klip di 360p, lalu generate semua klip | `K01.mp4` ... (tidak masuk git) | user |
| 7 | Narasi (VoxCPM2 clone) | `narasi.wav` (tidak masuk git) | user |
| 8 | Timing kata (faster-whisper) | `kata.json` atau `.srt` | user |
| 9 | Perakitan: klip + overlay angka + subtitle + audio | MP4 di `out/` | Claude |
| 10 | Pratinjau 20 detik, revisi, lalu render penuh | — | Claude + user |
| 11 | QC (cek angka vs narasi, audio, sumber ICW/PDF) | catatan di `naskah.md` | user + Claude |
| 12 | Kemasan: thumbnail, deskripsi + sumber, pinned comment | `upload.md` | Claude |
| 13 | Upload + potongan Shorts | baris baru di `LOG.md` | user |

Gerbang persetujuan: naskah disetujui sebelum storyboard; satu klip uji 360p sebelum generate semua; pratinjau 20 detik sebelum render penuh.

## Memulai sesi baru
Cukup tulis:
> Baca CLAUDE.md. Kita lanjut video NNN: <judul>, tahap <nomor>.
