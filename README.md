# 📚 Sistem Manajemen Toko Buku (CLI + MySQL)

Project ini merupakan Sistem Manajemen Toko Buku berbasis Command Line Interface (CLI) yang dibuat menggunakan Python, MySQL, dan Pandas.

Project ini dikembangkan sebagai Capstone Project Module 1 pada program AI Engineer Bootcamp Purwadhika.

Aplikasi ini memungkinkan pengguna untuk mengelola data buku, stok buku di setiap cabang, pengguna (member/non-member), transaksi penjualan, serta menampilkan statistik penjualan buku.

## 🎯 Tujuan Project

Project ini dibuat untuk mempraktikkan beberapa konsep dasar dalam pengembangan aplikasi berbasis data, seperti:

Penggunaan Python untuk aplikasi CLI

Pengelolaan database relasional menggunakan MySQL

Penggunaan SQL JOIN dan transaksi

Pengolahan data menggunakan Pandas

Visualisasi data menggunakan Matplotlib / Seaborn

Struktur kode Python yang modular

## ⚙️ Teknologi yang Digunakan
| Teknologi              | Kegunaan                        |
| ---------------------- | ------------------------------- |
| Python                 | Bahasa pemrograman utama        |
| MySQL                  | Database untuk penyimpanan data |
| Pandas                 | Pengolahan data                 |
| Matplotlib / Seaborn   | Visualisasi data                |
| mysql-connector-python | Koneksi Python ke MySQL         |

## 🗂️ Struktur Database

Database yang digunakan bernama bookstore_db dengan beberapa tabel utama:

| Tabel         | Deskripsi                            |
| ------------- | ------------------------------------ |
| `books`       | Menyimpan data buku                  |
| `book_genres` | Menyimpan kategori buku              |
| `branches`    | Menyimpan data cabang toko buku      |
| `book_stocks` | Menyimpan stok buku di setiap cabang |
| `users`       | Menyimpan data pengguna/member       |
| `book_sales`  | Menyimpan data transaksi penjualan   |

## 🚀 Fitur Aplikasi
### 1️⃣ Manajemen Buku

- Menambahkan buku baru

- Melihat daftar buku
- Menyimpan informasi buku seperti:
    - nama buku
    - harga
    - penulis
    - genre

### 2️⃣ Manajemen Cabang dan Stok

- Mengelola data cabang toko buku
- Menyimpan stok buku di setiap cabang
- Mengurangi stok setelah transaksi

### 3️⃣ Manajemen Pengguna

- Menyimpan data pengguna
- Mendukung transaksi:
  - member
  - non-member

Member dapat redeem point saat transaksi.

### 4️⃣ Transaksi Penjualan

- Fitur transaksi memungkinkan pengguna untuk:
  - Membeli beberapa buku dalam satu transaksi
  - Menghitung otomatis:
  - jumlah buku
  - harga
  - total pembayaran
  - Mengurangi stok buku secara otomatis

### 5️⃣ Statistik Penjualan

- Aplikasi juga menyediakan fitur visualisasi data penjualan, seperti:
  - Total penjualan buku
  - Distribusi penjualan buku
  - Analisis sederhana menggunakan Pandas dan Matplotlib

## Konfigurasi Koneksi Database
```Python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="bookstore_db"
)
```