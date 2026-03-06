from .genres import add_genre
from .books import add_book
from .branches import add_branch
from .book_stocks import add_book_stock, update_book_stock_by_branch

"""
Menu ini sebelumnya adalah add_data, tetapi diubah menjadi data_management karena operasi pada menu ini tidak hanya add data, tetapi juga akan ada update data
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
        print("2. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-2): "))

        if choice == 1:
            add_book(connection)
        elif choice == 2:
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
        print("1. Tambah stok buku per cabang")
        print("2. Perbarui stok buku per cabang")
        print("3. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-3): "))

        if choice == 1:
            add_book_stock(connection)
        elif choice == 2:
            update_book_stock_by_branch(connection)
        elif choice == 3:
            break
        else:
            print("Pilihan tidak valid")

def user_menu(connection):
    pass

def transaction_menu(connection):
    pass