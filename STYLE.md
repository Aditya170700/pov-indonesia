# STYLE

> Status: gaya visual, maskot (Wowo v4), dan alur klip Flow sudah diputuskan. Bagian grafis, thumbnail, dan audio masih draf.

## Kanvas
- 1920×1080, 30 fps (video panjang); 1080×1920 (potongan pendek).
- **Gaya visual: A2.2 Cinematic Story.** Adegan utama berupa klip video AI (Google Flow, Omni Flash) dengan latar berwarna sinematik. Grafis, angka, subtitle, dan perakitan dibuat dari kode (`engine/`, Chrome headless + ffmpeg).

## Warna
| Peran | Hex | Pemakaian |
|---|---|---|
| Latar gelap | `#14213D` | latar default adegan |
| Latar terang | `#F5F1E8` | adegan kertas/dokumen |
| Merah aksen | `#E63946` | angka buruk, peringatan, korupsi |
| Hijau aksen | `#2A9D8F` | angka baik, perbaikan |
| Kuning highlight | `#FFC93C` | kata aktif di subtitle, teks thumbnail |
| Putih teks | `#FFFFFF` | teks utama |
| Hitam outline | `#0B0B0B` | outline teks |

## Font
- Judul dan angka besar: **Poppins ExtraBold**
- Subtitle dan teks biasa: **Poppins Bold**

## Subtitle
- Kata per kata mengikuti `kata.json`.
- Huruf kapital, putih, outline hitam tebal.
- Kata yang sedang diucapkan: latar kotak kuning `#FFC93C`, teks hitam.
- Posisi tengah bawah, maksimal 6 kata per tampilan.

## Maskot
- **Nama: Wowo** (karakter fiktif, tidak meniru tokoh nyata atau karakter berhak cipta mana pun).
- **Desain v4 (stickman murni + topi merah, disetujui):**
  - Kepala bulat putih-gading `#F5F1E8` dengan garis hitam tipis, dua mata titik, senyum kecil.
  - Topi merah `#E63946` ala baseball dengan brim pendek ke depan, **tanpa tulisan** (teks tidak andal di klip AI).
  - Badan, lengan, dan kaki berupa garis hitam tebal seragam; tanpa baju dan celana.
  - Karakter pendukung: stickman abu-abu polos tanpa topi (warga, petugas, pekerja).
- **Rig kode:** `engine/wowo.js` (varian `stick`). Lembar referensi: `assets/wowo-ref.png` (dipakai sebagai gambar referensi karakter di Flow untuk SETIAP klip).
- **Pose di rig:** netral, jalan, kaget (mata bulat, mulut "o", tangan terangkat), menunjuk, bicara. Pose lain ditambah sesuai kebutuhan.
- Tulisan "WOWO" hanya muncul lewat overlay kode (intro, thumbnail), bukan di klip AI.
- Varian lama (v3: kulit sawo, kaus merah WOWO) tetap ada di rig (`variant: 'kaus'`) untuk adegan kode. Maskot tidak boleh digambar ulang di luar `engine/wowo.js` dan `assets/wowo-ref.png`.

### Kunci karakter untuk prompt Flow
Dipakai persis di tiap prompt (lihat `videos/001-bebas-korupsi/flow-prompts.md`): round off-white head with thin black outline, two dot eyes, small smile, bright red baseball-style cap with short brim (no text), thin black stick body and limbs of constant line weight, no clothes.

## Grafis penjelas (komponen kode di `engine/`, dibuat bertahap)
- `Kalender` — "HARI KE-…", "TAHUN KE-…"
- `ChatHP` — tampilan chat WhatsApp/notifikasi berita
- `AngkaBesar` — angka/statistik dengan animasi hitung
- `Headline` — potongan judul berita fiktif (diberi label "ilustrasi")
- `PetaIndonesia` — sorotan provinsi/kota

## Thumbnail
- Maskot dengan ekspresi kuat di satu sisi.
- Teks maksimal 4 kata, kuning/putih, outline hitam, diakhiri "?" atau "!".
- Latar kontras dengan objek simbolik topiknya.

## Audio
- Narasi selalu paling dominan.
- Musik latar jauh lebih pelan dari narasi (sekitar -20 dB di bawahnya); SFX secukupnya.
- Pelajaran dari kompetitor: penonton protes kalau backsound/SFX lebih keras dari narasi.
