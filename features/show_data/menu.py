from .genres import show_genre_data
from .books import show_book_data
from .branches import show_branch_data
from .book_stocks import show_book_stock_data
from .book_sales import show_sales_data
from .users import show_member_data

"""
Pada menu ini tidak hanya akan menampilkan data secara keseluruhan, tapi nanti bisa menampilkan data berdasarkan sesuatu, sehingga di sini akan ada improvement yaitu membuat submenu kembali berdasarkan data, misalnya submenu data genre buku

1. Data genre:
    - Keseluruhan
    - Berdasarkan tipe (fiction atau non-fiction)

2. Data buku:
    - Keseluruhan
    - Berdasarkan author
    - Berdasarkan genre
    - Berdasarkan genre_type
    - Berdasarkan harga (lebih murah atau mahal) -> user memutuskan untuk filter apakah lebih murah atau lebih mahal dari harga yang diinput
    - Berdasarkan range harga (range sesuai inputan user)

3. Data cabang
    - Keseluruhan
    - Berdasarkan kota
    - Berdasarkan provinsi

4. Data stok buku
    - Keseluruhan
    - Berdasarkan jumlah stok
    - Berdasarkan range jumlah stok
    - Berdasarkan nama buku
    - Berdasarkan cabang

    Mungkin bisa dijadikan satu function (filter), berarti boleh ada inputan yang kosong, agar tidak kebanyakan pilihan menu

5. Data penjualan
    - Keseluruhan
    - Berdasarkan buku
    - Berdasarkan genre
    - Berdasarkan cabang
    - Berdasarkan kota
    - Berdasarkan provinsi
    - Berdasarkan user
    - Berdasarkan tanggal 

    Ada beberapa yang bisa dijadikan satu function (filter), berarti boleh ada inputan yang kosong, agar tidak kebanyakan pilihan menu

6. Data member
    - Keseluruhan
    - Berdasarkan no. telepon
    - Berdasarkan email
    - Berdasarkan points
    - Berdasarkan range points
    - Berdasarkan tier

Catatan: Masih optional, yang penting bisa menampilkan data secara keseluruhan dulu
"""

def menu(connection):
    while True:
        print("\n=== MENU TAMPILKAN DATA ===\n")
        print("1. Data genre buku")
        print("2. Data buku")
        print("3. Data cabang")
        print("4. Data stok buku")
        print("5. Data penjualan")
        print("6. Data member")
        print("7. Kembali ke menu utama")
    
        choice = int(input("Masukkan pilihan anda (1-7): "))

        if choice == 1:
            show_genre_data(connection)
        elif choice == 2:
            show_book_data(connection)
        elif choice == 3:
            show_branch_data(connection)
        elif choice == 4:
            show_book_stock_data(connection)
        elif choice == 5:
            show_sales_data(connection)
        elif choice == 6:
            show_member_data(connection)
        elif choice == 7:
            break
        else:
            print("Pilihan tidak valid")