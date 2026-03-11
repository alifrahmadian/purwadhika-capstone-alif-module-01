from .menus.books import menu as book_menu
from .menus.book_stocks import menu as book_stock_menu

def menu(connection):
    while True:
        print("\n=== VISUALISASI DATA ===")
        print("1. Data buku")
        print("2. Data stok buku")
        print("3. Data transaksi buku")
        print("4. Data user")
        print("5. Kembali ke menu utama")

        choice = int(input("Masukkan pilihan anda (1-5): "))

        if choice == 1:
            book_menu(connection)
        elif choice == 2:
            book_stock_menu(connection)
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            break
        else:
            print("Pilihan tidak valid")