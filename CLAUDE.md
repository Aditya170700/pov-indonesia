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
- Satu video = satu folder `videos/NNN-slug/`, salin dari `videos/_template/`.
- Kerjakan per tahap (lihat alur di `CHANNEL.md`). Hasil tiap tahap disimpan ke file di folder video, bukan hanya di chat.
- Jangan mengarang fakta. Setiap angka atau klaim faktual di naskah harus punya sumber di `riset.md` dengan ID `[S1]`, `[S2]`, dst.
- Angka yang tampil di layar (`adegan.json`) harus sama persis dengan yang diucapkan di naskah.
- Maskot, subtitle, dan thumbnail selalu memakai komponen yang sudah ada di `remotion/`. Jangan menggambar ulang maskot dari nol.
- Setelah video selesai, tambahkan barisnya di `LOG.md`.
