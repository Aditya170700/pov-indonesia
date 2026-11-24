# TEMPLATE NASKAH

Target: 1.500–1.800 kata (≈10–13 menit, ±140 kata/menit). Bahasa santai, menyapa "kamu".

Prinsip: isi video harus **melampaui** yang dibayangkan penonton dari judul dan thumbnail. Tiap bagian harus memberi alasan untuk terus menonton: pertanyaan yang dibuka (open loop), lalu dibayar (payoff) sambil membuka pertanyaan baru. Aturan angka di bawah adalah pedoman umum, bukan hasil data channel kita; koreksi setelah ada grafik retensi dari YouTube Studio.

## Sebelum menulis (wajib)
1. **Paket judul + thumbnail:** tulis 3 judul dan 3 konsep thumbnail (teks + gambar), satu sudut per varian, mengikuti `STYLE.md` bagian "Judul dan thumbnail". Judul memberi janji; naskah harus membayarnya.
2. **Janji video** satu kalimat, dan **emosi utama** (mis. lega, kaget, resah, geli).
3. **Fakta kejutan:** di `riset.md`, beri skor kejutan 1–100 per fakta (80+ = emas, 50–79 = pendukung, <50 dibuang). Kumpulkan 5–10 fakta kuat. Hook dan klimaks dibangun dari yang skornya tertinggi.
4. **Peta open loop:** daftar pertanyaan yang dibuka di hook dan babak, dan di bagian mana tiap pertanyaan dijawab.

## Struktur (dengan acuan menit untuk 10–13 menit)

### 1. Hook (0:00–0:25)
- Mulai dari situasi konkret yang dirasakan "kamu" (bukan pengantar abstrak). Tanpa salam, tanpa sapaan channel.
- Sebut taruhan dan satu pertanyaan yang harus dijawab, lalu bayangan twist ("tapi ada satu hal yang justru memburuk, dan itu ada di menit ke-X").
- Tulis **3 varian hook** (kontra-intuitif, cerita, angka mengejutkan). Pilih satu bersama pemilik repo.
- Tidak ada ajakan subscribe atau sponsor di 60 detik pertama.

### 2. Aturan skenario + re-hook (0:25–1:15)
- Aturan dunia baru dalam 2–3 kalimat. Satu fakta pembanding `[S#]`, jangan lebih; jangan tumpuk angka di sini.
- Re-hook: jelaskan kenapa ini penting sekarang dan apa yang akan dilihat berikutnya.

### 3. Babak bertahap (1:15–±60% durasi): 5–7 babak
Misalnya: Hari 1 → Minggu 1 → Bulan 1 → Tahun 1 → 10 Tahun. Setiap babak:
- Apa yang **kamu** alami langsung (dompet, pekerjaan, keluarga, lingkungan), dengan satu detail kecil yang relate.
- Satu fakta atau angka jangkar `[S#]`.
- **Payoff kecil** (jawaban atas pertanyaan sebelumnya) **dan satu pertanyaan baru** di akhir babak.
- Re-hook tiap 30–60 detik: kalimat pendek yang menjanjikan sesuatu di depan ("dan di sini mulai tidak sesederhana itu").
- Urutkan babak dari yang kuat ke yang paling kuat; simpan fakta terbaik untuk menjelang akhir.

### 4. Twist / sisi lain (±60%–85% durasi)
- Konsekuensi tak terduga atau hambatan realistis. Video tidak boleh terlalu utopis.
- Bayangannya sudah disebut di hook; di sini dibayar tuntas.
- Disarankan 2 twist kecil, bukan satu twist besar di ujung.

### 5. Klimaks + penutup (±85%–100%)
- Bayar janji hook (jawaban utama) dalam 1–2 kalimat jelas.
- **Pancingan komentar ringan** (juga untuk pinned comment): pilihan A/B atau pengalaman pribadi yang bisa dijawab dalam satu kalimat. Netral; jangan memihak partai atau tokoh.
- **Teaser video berikutnya** (binge loop): buka satu pertanyaan baru yang dijawab di video lain. Tanpa "kesimpulannya" dan tanpa "terima kasih sudah menonton".

## Humor dan pembanding relatable
- Setelah angka besar, beri **pembanding** yang dikenal penonton (mis. "uang segitu setara N mangkok mie ayam untuk tiap orang Indonesia"). Boleh sarkas ringan, satu momen per babak, dan berfungsi sebagai pemecah ritme.
- Setiap pembanding adalah klaim faktual: input (harga, jumlah penduduk, dsb.) harus punya sumber dan tanggal di `riset.md`, tabel **Pembanding**, lengkap dengan rumus. Hitungan dijalankan lewat kode, bukan perkiraan. Tulis hasil dibulatkan dan sebut "kira-kira".
- Utamakan pembanding yang awet (biaya bangun puskesmas atau sekolah, harga tol per km, gaji guru per tahun, harga mie ayam) daripada yang cepat basi (nilai pasar pemain). Jangan menggambar atau menampilkan tokoh nyata.
- Sarkasme diarahkan ke sistem dan kebijakan, bukan ke individu, suku, atau agama. Humor tidak boleh membuat korupsi atau korbannya terasa remeh.
- Angka hasil hitungan yang tampil di layar (kartu hitungan) harus sama persis dengan narasi.

## Ritme visual (untuk storyboard)
- Ganti visual atau audio tiap 4–8 detik (ganti klip, zoom/punch-in dari kode, kartu angka, pill teks, SFX). Cue visual minimal tiap 10 detik.
- Klip Flow boleh 6–10 detik, tapi di dalamnya dipecah dengan overlay atau zoom sesuai ritme di atas.
- Tiap paragraf ditandai perkiraan detiknya, supaya durasi klip dipesan pas (selisih ideal 0–1 dtk dari narasi).

## Format penulisan
- Paragraf pendek, satu paragraf = satu tarikan napas narator. Tulis dengan format: `## Babak: ...` lalu paragraf, dan di akhir paragraf `(±N dtk)`.
- Tandai sumber dengan `[S1]`, `[S2]` sesuai `riset.md`; dihapus sebelum masuk TTS.
- Angka ditulis seperti diucapkan.
- Bahasa percakapan: kalimat pendek, kosakata sederhana, kalimat aktif.

## Pemeriksaan sebelum minta persetujuan
- [ ] 3 judul + 3 konsep thumbnail + janji video tertulis; tidak ada kata/angka yang sama antara judul dan teks thumbnail
- [ ] 3 varian hook; hook memberi nilai dalam 3 detik pertama dan membuka pertanyaan
- [ ] Peta open loop: tiap pertanyaan terjawab
- [ ] Re-hook minimal tiap 60 detik; tidak ada bagian >60 detik tanpa fakta atau perubahan
- [ ] Twist tidak hanya di menit terakhir
- [ ] Penutup: payoff + pancingan ringan + teaser, tanpa kesimpulan formal
- [ ] Pembanding relatable punya sumber, rumus, dan hasil hitung kode
- [ ] Jumlah kata sesuai target; angka punya sumber

## Contoh naskah terbaik
(Diisi setelah video yang dirilis punya grafik retensi bagus. Contoh nyata membuat gaya antar video jauh lebih konsisten.)
