from .genres import add_genre
from .books import add_book
from .branches import add_branch
from .book_stocks import (
    add_book_stock, 
    add_book_stock_amount_by_branch,
    )

"""
Menu ini merupakan menu manajemen data, di mana operator toko dapat melakukan berbagai manajemen data seperti menambahkan dan meng-update data yang tersedia.
"""

def menu(connection):
    while True:
        print("\n=== MANAJEMEN DATA ===")
        print("1. Data genre")
        print("2. Data buku")
        print("3. Data cabang")
        print("4. Data stok buku per cabang")
        print("5. Data user/member")
        print("6. Transaksi buku")
        print("7. Kembali ke menu utama")

        choice = int(input("Masukkan pilihan anda (1-7): "))

        if choice == 1:
            genre_menu(connection)
        elif choice == 2:
           book_menu(connection)
        elif choice == 3:
            branch_menu(connection)
        elif choice == 4:
            book_stock_menu(connection)
        elif choice == 5:
            user_menu(connection)
        elif choice == 6:
            transaction_menu(connection)
        elif choice == 7:
            break
        else:
            print("Pilihan tidak valid")

def genre_menu(connection):
    while True:
        print("\n=== DATA GENRE ===")
        print("1. Tambah genre")
        print("2. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-2): "))

        if choice == 1:
            add_genre(connection)
        elif choice == 2:
            break
        else:
            print("Pilihan tidak valid")

def book_menu(connection):
    while True:
        print("\n=== DATA BUKU ===")
        print("1. Tambah buku")
        print("2. Update harga buku")
        print("3. Tambah stok buku yang bisa disebarkan ke cabang (reserved)")
        print("4. Ubah nama buku")
        print("5. Ubah nama penulis buku")
        print("6. Ubah genre buku")
        print("7. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-7): "))

        if choice == 1:
            add_book(connection)
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            break
        else:
            print("Pilihan tidak valid")
 

def branch_menu(connection):
    while True:
        print("\n=== DATA CABANG ===")
        print("1. Tambah cabang")
        print("2. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-2): "))

        if choice == 1:
            add_branch(connection)
        elif choice == 2:
            break
        else:
            print("Pilihan tidak valid")


def book_stock_menu(connection):
     while True:
        print("\n=== DATA STOK BUKU ===")
        print("1. Daftar stok buku per cabang")
        print("2. Tambah jumlah stok buku per cabang")
        print("3. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-3): "))

        if choice == 1:
            add_book_stock(connection)
        elif choice == 2:
            add_book_stock_amount_by_branch(connection)
        elif choice == 3:
            break
        else:
            print("Pilihan tidak valid")

def user_menu(connection):
    pass

def transaction_menu(connection):
    pass