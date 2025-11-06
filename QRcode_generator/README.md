#Pembuat Kode QR Sederhana (Simple QR Code Generator) 🐍
Sebuah skrip Python sederhana berbasis terminal (CLI) untuk membuat gambar Kode QR dari input teks atau URL.

#📜 Tentang Proyek
Proyek ini adalah alat sederhana yang memungkinkan pengguna untuk dengan cepat mengubah data teks, seperti link website, nomor telepon, atau pesan singkat, menjadi sebuah gambar Kode QR yang bisa disimpan. Program ini sepenuhnya berjalan di terminal.

#✨ Fitur
Interaktif: Meminta input dari pengguna untuk data yang akan di-encode.

Kustomisasi Nama File: Pengguna dapat menentukan sendiri nama file untuk gambar Kode QR yang akan disimpan.

Sederhana: Kode yang ringan dan mudah dipahami, cocok untuk pemula.

Dependensi Minimal: Hanya memerlukan pustaka qrcode dan Pillow.

#🚀 Cara Menggunakan
Untuk menjalankan proyek ini di komputermu, ikuti langkah-langkah berikut:

Clone Repositori Ini

Bash

git clone https://github.com/namapengguna-kamu/nama-repo-kamu.git
cd nama-repo-kamu
Buat dan Aktifkan Virtual Environment

Bash

# Membuat environment (cukup sekali)
python -m venv venv

# Mengaktifkan di Windows
venv\Scripts\activate

# Mengaktifkan di macOS/Linux
source venv/bin/activate
Install Dependensi yang Dibutuhkan
Pastikan kamu sudah membuat file requirements.txt. Jika belum, jalankan perintah ini di terminalmu:

Bash

pip freeze > requirements.txt
Setelah file dibuat, install dengan perintah:

Bash

pip install -r requirements.txt
Jalankan Skrip

Bash

python qrcode_generator.py
Ikuti Instruksi
Program akan memintamu untuk memasukkan teks/URL dan nama file yang diinginkan. Setelah itu, gambar Kode QR akan tersimpan di dalam folder proyek.

🛠️ Teknologi yang Digunakan
Python

Pustaka qrcode: Untuk logika pembuatan Kode QR.

Pustaka Pillow: Untuk memproses dan menyimpan file gambar.
