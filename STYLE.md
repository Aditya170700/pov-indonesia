# STYLE

> Status: gaya visual, maskot (Wowo v4), alur klip Flow, subtitle, dan grafis sudah diuji di pilot 001. Aturan judul + thumbnail (paket A/B) ditetapkan 24 Nov 2026. Musik latar masih draf.

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
Dipakai persis di tiap prompt (lihat `videos/testing/flow-prompts.md`): round off-white head with thin black outline, two dot eyes, small smile, bright red baseball-style cap with short brim (no text), thin black stick body and limbs of constant line weight, no clothes.

## Grafis penjelas (sudah ada di `engine/overlay.html`; tipe dipanggil lewat `overlay.json`)
- `kal` (kalender) — "HARI KE-…", "TAHUN KE-…"
- `notif` — kartu notifikasi berita (selalu berlabel ILUSTRASI)
- `stat` — kartu angka dengan animasi hitung, label, dan baris sumber; `pill` — catatan pendek (warna opsional `bg`/`fg`); `judul` — kartu judul di awal; `tanya` — pertanyaan komentar di akhir
- Ditambah di video 001: `hitung` (baris operasi muncul satu per satu, baris `hasil` besar), `bar` (batang horizontal tumbuh saat angkanya diucapkan; opsional `tag`), `sim` (label SIMULASI SEDERHANA + keterangan asumsi), `jawab` (cap besar "TIDAK" + kalimat jawaban + baris hijau), `teaser` (video berikutnya, masuk dari kanan)
- Teks kartu otomatis dikecilkan kalau tidak muat lebar kartu. Cek posisi kartu terhadap kepala Wowo per klip sebelum render penuh.
- Koreksi ejaan subtitle per video: `videos/NNN/koreksi.json` (`[["dari", "ke"], ...]`, boleh beberapa kata), dipakai `komposit.py` setelah daftar `FIX` global.
- Belum ada: `PetaIndonesia` (sorotan provinsi/kota), `Headline` (judul berita fiktif)

## Judul dan thumbnail (paket uji A/B)

Setiap video panjang WAJIB punya **3 judul** dan **3 thumbnail** yang berbeda, untuk diuji di YouTube Studio (Uji & Bandingkan). Ketiganya ditulis di tahap 3 (konsep) dan dibuat di tahap 12 (`upload.md`).

### Tiga sudut (satu sudut per varian)
| Varian | Judul | Thumbnail |
|---|---|---|
| A | Skenario/pertanyaan ("Gimana jadinya kalau…?") | Angka paling mengejutkan (mis. "Rp279 TRILIUN BOCOR!") |
| B | Angka/hasil ("279 Triliun…") | Perbandingan/visual (mis. Indonesia vs Singapura, "126 TAHUN?") |
| C | Perbandingan/konflik ("…Bisa Nyusul Singapura?") | Wowo ekspresi kuat + satu pertanyaan pendek |

Pasangan varian di tabel hanya titik awal; yang penting tiap judul dan tiap thumbnail punya sudut berbeda, bukan sekadar ganti kata.

### Aturan judul
- Maks. **70 karakter** (ideal 45–60). Kata kunci topik (mis. "korupsi", "pajak") wajib ada di ketiga judul dan berada di **40 karakter pertama**, karena judul terpotong di HP.
- Angka ditulis dengan digit ("279 Triliun", "10 Tahun"), bukan huruf.
- Huruf besar di awal kata (Title Case). Maks. 1 tanda seru per judul; tidak ada kata yang SELURUHNYA KAPITAL.
- Janji judul harus terjawab di video (tidak clickbait palsu). Angka di judul harus sama dengan angka di narasi.
- Pola lama `POV: <skenario>, Ini yang Terjadi` boleh dipakai sebagai salah satu varian, tidak wajib.

### Aturan thumbnail
- **Warna latar: biru tua**, gradasi `#1B2B52` ke `#14213D` (boleh pola sinar/rays). Jangan latar merah dominan: tenggelam di tampilan YouTube yang merah-putih. Merah `#E63946` hanya untuk aksen (label, bendera, peringatan).
- **Teks:** kuning `#FFC93C` untuk teks utama, putih untuk keterangan; Poppins Bold dengan outline hitam tebal (±16% ukuran huruf).
- **Jumlah kata:** teks besar maks. **3 kata/angka**, keterangan kecil maks. **3 kata**; total maks. 6 kata. Satu ide per thumbnail.
- **Wowo wajib ada**, ekspresi kuat (kaget, panik, lari), digambar dari `engine/wowo.js`. Tidak ada foto tokoh nyata, logo partai, atau logo media.
- **Zona aman:** pojok kanan bawah ±200×80 px dibiarkan kosong (label durasi YouTube).
- **Uji ukuran kecil:** perkecil ke lebar 246 px (ukuran di daftar rekomendasi); teks utama harus tetap terbaca.
- File: PNG 1280×720, < 2 MB, disimpan di `out/NNN-thumb-A.png`, `-B.png`, `-C.png`.
- Pembuatan: `engine/thumb.html` (contoh dari video 001; salin fungsi `drawA`/`drawB`, ganti teks dan objek) lalu `python3 engine/thumb.py A B C`.

### Aturan silang judul × thumbnail
- **Tidak boleh ada kata atau angka yang sama** antara teks thumbnail mana pun dan judul mana pun dalam satu paket (kecuali kata fungsi: di, ke, dari, yang, dan, untuk, buat). Alasannya: saat uji A/B, judul dan thumbnail mana pun bisa tampil berpasangan, jadi thumbnail harus menambah informasi, bukan mengulang judul.
  - Contoh salah: judul "279 Triliun Terselamatkan!…" + thumbnail "Rp279 TRILIUN".
  - Contoh benar: judul "Gimana Jadinya Kalau Indonesia Nol Korupsi…?" + thumbnail "126 TAHUN? buat nyusul Singapura".
- Judul dan thumbnail tetap membicarakan janji yang sama; jangan sampai thumbnail menjanjikan hal yang tidak ada di video.

### Cara menjalankan uji A/B
1. Upload dengan judul A + thumbnail A.
2. YouTube Studio → video → **Uji & Bandingkan**. Kalau tersedia uji gabungan judul + thumbnail, pasangkan A-A, B-B, C-C. Kalau tidak, uji judul dulu; setelah ada pemenang, uji 3 thumbnail.
3. Selama uji berjalan, jangan ganti judul atau thumbnail secara manual.
4. Catat pemenang (judul dan thumbnail) dan CTR-nya di `LOG.md`. Setelah ±5 video, lihat sudut mana yang paling sering menang dan koreksi tabel "Tiga sudut" di atas.

## Audio
- Narasi selalu paling dominan.
- Musik latar jauh lebih pelan dari narasi (sekitar -20 dB di bawahnya); SFX secukupnya.
- Pelajaran dari kompetitor: penonton protes kalau backsound/SFX lebih keras dari narasi.
- Narasi dinormalkan ke -16 LUFS oleh `komposit.py` (file `narasi-norm.wav`). Audio bawaan klip Flow dibuang. Musik latar belum dipakai di pilot; kalau dipakai, simpan di `assets/` dan turunkan sekitar -20 dB dari narasi.

## Resolusi klip
- Generate klip Flow di 360p, upscale ke 720p lewat Flow, lalu `rakit.py` menaikkan ke 1080p (lanczos). Cukup tajam untuk gaya stickman. Teks, angka, dan subtitle dirender langsung di 1080p dari kode.

## Pakai ulang klip
- Untuk video panjang, satu klip Flow (maks. 10 dtk) boleh dipakai di dua slot narasi yang berdekatan: slot kedua memakai punch-in 1,35x dan mulai dari detik ±3 (`timeline.json`: `ss`, `zoom`, `cx`, `cy`). Rencanakan klip yang bisa dipakai ulang dengan cara menempatkan Wowo dan objek utama di tengah frame.
