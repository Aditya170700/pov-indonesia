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
- **Judul + thumbnail:** tiap video panjang punya 3 judul dan 3 thumbnail untuk uji A/B. Aturan lengkap (sudut, panjang, warna, larangan kata yang sama) ada di `STYLE.md` bagian "Judul dan thumbnail".
  - Pola lama `POV: <skenario>, Ini yang Terjadi` boleh jadi salah satu varian judul.

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
   - Pembanding humor ("setara N mangkok mie ayam") juga klaim faktual: input bersumber, rumus dicatat di `riset.md`, hasil dihitung lewat kode. Sarkasme ke sistem, bukan ke individu, suku, atau agama.
6. Saat upload, aktifkan label konten AI (audio/visual sintetis).

## Alur produksi per video
Pembagian kerja: Claude = riset, naskah, storyboard, prompt klip, grafis dan perakitan (render di workspace Claude). Pemilik repo = rekam narasi (VoiceStudio) dan generate klip di Flow.

| # | Tahap | Hasil di `videos/NNN-slug/` | Siapa |
|---|---|---|---|
| 1 | Ide + judul | judul di `naskah.md` | Claude |
| 2 | Riset fakta + skor kejutan (5-10 fakta kuat) | `riset.md` | Claude |
| 3 | Naskah: 3 judul + 3 konsep thumbnail (aturan di `STYLE.md`), 3 varian hook, peta open loop (minta persetujuan) | `naskah.md` | Claude + user |
| 4 | Storyboard + peta narasi ke klip | `storyboard.md`, `adegan.json` | Claude |
| 5 | Prompt klip Flow | `flow-prompts.md` | Claude |
| 6 | Uji 1 klip di 360p, lalu generate semua klip (360p, upscale ke 720p di Flow) | `klip/K01.mp4` ... (tidak masuk git) | user |
| 7 | Narasi: VoiceStudio, fitur Cerita, naskah dari `narasi-bersih.md` | `narasi.mp3` (tidak masuk git; VoiceStudio menyimpannya di `~/.omnivoice/outputs/`) | user |
| 8 | Timing kata: `python3 engine/kata.py narasi.mp3` | `kata.json` | user |
| 9 | Perakitan: `timeline.json` + `overlay.json`, lalu `engine/rakit.py` (klip jadi `base.mp4`) dan `engine/komposit.py` (overlay + subtitle + audio) | MP4 di `out/` | Claude |
| 10 | Pratinjau 20 detik (`komposit.py --start 0 --dur 20`), revisi, lalu render penuh | — | Claude + user |
| 11 | QC (cek angka vs narasi, audio, sumber ICW/PDF) | catatan di `naskah.md` | user + Claude |
| 12 | Kemasan: 3 judul + 3 thumbnail (`engine/thumb.html`), deskripsi + sumber, pinned comment | `upload.md`, `out/NNN-thumb-A/B/C.png` | Claude |
| 13 | Upload, aktifkan Uji & Bandingkan (judul/thumbnail), potongan Shorts | baris baru di `LOG.md` (+ pemenang uji A/B) | user |

Gerbang persetujuan: naskah disetujui sebelum storyboard; satu klip uji 360p sebelum generate semua; pratinjau 20 detik sebelum render penuh.

## Memulai sesi baru
Cukup tulis:
> Baca CLAUDE.md. Kita lanjut video NNN: <judul>, tahap <nomor>.

## Catatan dari pilot 001
- Narasi memimpin: tiap klip diperlambat/dipercepat 0,9x-1,15x lalu dipotong atau dibekukan di frame terakhir. Karena itu durasi klip yang dipesan di storyboard sebaiknya sedikit lebih panjang dari estimasi narasi segmennya (selisih ideal 0-1 dtk), bukan jauh lebih panjang.
- Kredit Flow: 16 klip 360p (134 dtk) memakai 135 kredit; "tingkatkan resolusi" ke 720p tidak mengurangi kredit (diuji pengguna). Render penuh 130 dtk butuh ±2 menit di workspace.
- Panduan langkah untuk pemilik repo (Flow, VoiceStudio, kata.py): `PANDUAN.md`.
- Retensi: aturan struktur naskah (hook, re-hook tiap 30-60 dtk, open loop, ritme visual tiap 4-8 dtk, penutup dengan teaser) ada di `templates/naskah.md`. Setelah video rilis, catat di `LOG.md` menit berapa penonton paling banyak pergi, lalu koreksi template.
