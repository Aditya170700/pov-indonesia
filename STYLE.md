# STYLE

> Status: draf awal. Nilai di bawah adalah usulan; ubah sesuai selera, lalu semua video mengikuti file ini.

## Kanvas
- 1920×1080, 30 fps (video panjang); 1080×1920 (potongan pendek).
- Gaya visual: ilustrasi flat 2D, bentuk sederhana, dibuat lewat kode (SVG/Remotion).

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
- **[BELUM]** Desain final belum dibuat. Kriteria:
  - Laki-laki muda Indonesia, warga biasa (bukan pejabat).
  - Flat 2D, 1–2 ciri khas yang gampang dikenali dari jauh.
  - Pose minimal: `netral`, `bicara`, `kaget`, `menunjuk`, `sedih`, `senang`, `berpikir`.
- Setelah dibuat, maskot hanya dipanggil dari `remotion/src/components/Maskot.tsx`. Tidak boleh digambar ulang.

## Grafis penjelas (komponen siap pakai)
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
