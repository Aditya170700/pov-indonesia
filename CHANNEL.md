# CHANNEL

> Status: draf awal. Bagian bertanda **[BELUM]** perlu diputuskan.

## Identitas
- **Nama channel:** [BELUM] — nama kerja: POV Indonesia
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
| # | Tahap | Hasil di `videos/NNN-slug/` |
|---|---|---|
| 1 | Ide + judul | judul di `naskah.md` |
| 2 | Riset fakta | `riset.md` |
| 3 | Naskah | `naskah.md` |
| 4 | Daftar adegan | `adegan.json` |
| 5 | Narasi (VoxCPM2) | `narasi.wav` (tidak masuk git) |
| 6 | Timing kata (faster-whisper) | `kata.json` |
| 7 | Visual (Remotion) | kode adegan di `remotion/` |
| 8 | Preview + revisi | — |
| 9 | Musik + SFX | — |
| 10 | Render | `out/*.mp4` (tidak masuk git) |
| 11 | QC (tonton penuh, cek angka vs narasi) | catatan di `naskah.md` |
| 12 | Kemasan: thumbnail, deskripsi + sumber, pinned comment | `upload.md` |
| 13 | Upload + potongan Shorts | baris baru di `LOG.md` |

## Memulai sesi baru
Cukup tulis:
> Baca CLAUDE.md. Kita lanjut video NNN: <judul>, tahap <nomor>.
