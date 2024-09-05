# aaPanel Domain Importer

Skrip Python sederhana untuk mengimpor beberapa domain sekaligus ke aaPanel menggunakan API aaPanel.

[![GitHub stars](https://img.shields.io/github/stars/username/aapanel-domain-importer.svg)](https://github.com/username/aapanel-domain-importer/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/username/aapanel-domain-importer.svg)](https://github.com/username/aapanel-domain-importer/network/members)

## Developer

**Kurniawan**

[![Instagram](https://img.shields.io/badge/Instagram-%40sedotphp-E4405F?style=flat&logo=instagram&logoColor=white)](https://www.instagram.com/sedotphp)

Jika Anda memiliki pertanyaan atau ingin berkolaborasi, jangan ragu untuk menghubungi saya melalui Instagram.

## Dukung Proyek Ini

Jika Anda merasa proyek ini bermanfaat, pertimbangkan untuk memberikan dukungan dengan cara berikut:

- **Star Repository**: Klik tombol ⭐️ di bagian atas halaman untuk menunjukkan apresiasi Anda.
- **Fork Repository**: Jika Anda ingin berkontribusi atau membuat versi Anda sendiri, klik tombol 'Fork' di kanan atas halaman.

Dukungan Anda sangat berarti dan membantu proyek ini tumbuh!

## Deskripsi

Proyek ini berisi skrip Python yang memungkinkan pengguna untuk mengimpor daftar domain ke aaPanel secara otomatis. Ini sangat berguna ketika Anda perlu menambahkan banyak domain sekaligus ke instalasi aaPanel Anda.

## Fitur

- Impor beberapa domain sekaligus dari file teks
- Menggunakan API aaPanel untuk menambahkan domain
- Pelaporan status untuk setiap domain yang diimpor

## Persyaratan

- Python 3.6+
- Modul `requests` (dapat diinstal dengan `pip install requests`)
- Akses ke instalasi aaPanel dengan API yang diaktifkan

## Instalasi

1. Clone repositori ini:
   ```
   git clone https://github.com/username/aapanel-domain-importer.git
   cd aapanel-domain-importer
   ```

2. Instal dependensi yang diperlukan:
   ```
   pip install requests
   ```

## Penggunaan

1. Edit file `aapanel_importer.py` dan sesuaikan variabel berikut:
   - `AAPANEL_URL`: URL webhook aaPanel Anda
   - `API_KEY`: API key aaPanel Anda

2. Buat file `daftar_domain.txt` dan isi dengan daftar domain yang ingin Anda impor, satu domain per baris.

3. Jalankan skrip:
   ```
   python aapanel_importer.py
   ```

## Konfigurasi

Anda dapat menyesuaikan parameter default untuk setiap website yang dibuat dengan mengedit fungsi `add_website()` dalam skrip. Parameter yang tersedia meliputi:

- `path`: Path direktori root untuk website
- `type`: Jenis website (misalnya "PHP")
- `version`: Versi PHP
- `port`: Port yang digunakan

## Berkontribusi

Kontribusi selalu diterima! Silakan buka issue atau kirimkan pull request jika Anda ingin berkontribusi pada proyek ini.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detailnya.

## Peringatan

Gunakan skrip ini dengan hati-hati. Selalu buat backup dan uji terlebih dahulu pada lingkungan pengembangan sebelum menggunakannya pada server produksi.
