# Catatan validasi versi awal

- Data seed: 59 nomor SPK unik, total kuantitas 34.741; setiap total size cocok. Status awal seluruhnya draft; jadwal aktif tidak diisi dari tanggal sumber.
- 13 pengujian backend berbasis database sementara lulus. Termasuk restart tanpa duplikasi seed setelah nomor sumber diedit, kontrol kapasitas dan transisi status, batas transaksi proses, rework/idempotency, impor atomik, serta backup yang dapat dibaca sebagai SQLite.
- Browser Chromium: pencarian/filter order, preview impor workbook asli (59 identik), membuat order baru, mengisi planning, release, kunci planning, cutting/sewing/packing/delivery, penutupan order, CSV dan backup diuji pada database sementara. Tidak ada error JavaScript pada alur tersebut.
- Tampilan desktop 1440 px dan mobile 390 px diperiksa; tabel lebar dapat digeser horizontal dan detail bisa dibuka melalui identitas order. Tidak ada overflow horizontal pada keseluruhan halaman mobile.
- Cetak satu SPK contoh menghasilkan PDF satu halaman A4. Ini bukan jaminan setiap catatan panjang akan muat satu halaman.
- Server dan launcher dijalankan pada Linux/Python 3.12. Windows/macOS tidak tersedia untuk pengujian langsung; launcher lintas platform dan instruksi telah disediakan.
- Database utama tidak diisi transaksi contoh pengujian. Approval sumber, arti tanggal, dan kebenaran dokumen teknik tetap memerlukan verifikasi manusia.

- Paket ZIP diekstrak ke folder bersih; launcher membuat venv baru, memasang seluruh versi dependensi yang dipin, dan menjalankan server. API menghasilkan 59 order draft / kuantitas 34.741; 13 pengujian backend juga lulus pada hasil ekstraksi.
