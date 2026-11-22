# Instruksi untuk Claude

Repo ini adalah dapur produksi channel YouTube video simulasi POV bertema politik dan tata kelola Indonesia.
Semua yang harus konsisten antar sesi disimpan di file, bukan di ingatan chat.

## Wajib dibaca di awal setiap sesi
1. `CHANNEL.md` — identitas channel, gaya bahasa, aturan konten.
2. `STYLE.md` — aturan visual, subtitle, maskot, thumbnail, audio.
3. `LOG.md` — video yang sudah dibuat (hindari topik dobel, lanjutkan pola judul).
4. Untuk tahap naskah: `templates/naskah.md`.

## Aturan kerja
- Bahasa komunikasi dengan pemilik repo: bahasa Indonesia santai.
- Satu video = satu folder `videos/NNN-slug/`, salin dari `videos/_template/`. Nomor 001 dipakai video pertama yang benar-benar dirilis; `videos/testing/` adalah video uji workflow (arsip, bukan nomor).
- Kerjakan per tahap (lihat alur di `CHANNEL.md`). Hasil tiap tahap disimpan ke file di folder video, bukan hanya di chat.
- Jangan mengarang fakta. Setiap angka atau klaim faktual di naskah harus punya sumber di `riset.md` dengan ID `[S1]`, `[S2]`, dst.
- Angka yang tampil di layar (`adegan.json`) harus sama persis dengan yang diucapkan di naskah.
- Maskot Wowo, subtitle, dan grafis selalu memakai kode di `engine/` dan `assets/wowo-ref.png`. Jangan menggambar ulang maskot dari nol. Tidak memakai Remotion.
- Klip adegan dibuat di Google Flow oleh pemilik repo dari prompt di `flow-prompts.md`; Claude tidak bisa menjalankan Flow. Setiap prompt wajib berdiri sendiri dan memuat kunci karakter dari `STYLE.md`.
- Teks, angka, dan logo tidak boleh muncul di klip AI; semuanya lewat overlay kode.
- Alur dan gerbang persetujuan (naskah, uji 360p, pratinjau 20 detik) ada di `CHANNEL.md`.
- Perakitan video: isi `timeline.json` dan `overlay.json` di folder video, lalu `python3 engine/rakit.py videos/NNN-slug` (klip jadi `base.mp4`; satu klip boleh dipakai ulang di beberapa entri timeline lewat field `ss`, `zoom`, `cx`, `cy`) dan `python3 engine/komposit.py videos/NNN-slug out/NNN.mp4 [--start S --dur D]` (overlay, subtitle kata per kata, narasi; Chrome headless + ffmpeg). `engine/render.py` hanya untuk adegan kode murni (maskot di `wowo.js`).
- Setelah video selesai, tambahkan barisnya di `LOG.md`.
