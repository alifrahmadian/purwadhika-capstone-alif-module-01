from .menus.books import menu as book_menu
from .menus.book_stocks import menu as book_stock_menu
from .menus.book_sales import menu as book_sales_menu

def menu(connection):
    while True:
        print("\n=== VISUALISASI DATA ===")
        print("1. Data buku")
        print("2. Data stok buku")
        print("3. Data transaksi buku")
        print("4. Kembali ke menu utama")

        choice = int(input("Masukkan pilihan anda (1-4): "))

        if choice == 1:
            book_menu(connection)
        elif choice == 2:
            book_stock_menu(connection)
        elif choice == 3:
            book_sales_menu(connection)
        elif choice == 4:
            break
        else:
            print("Pilihan tidak valid")