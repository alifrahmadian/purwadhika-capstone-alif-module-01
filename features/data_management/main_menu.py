from .menus.genres import menu as genre_menu
from .menus.books import menu as book_menu
from .menus.branches import menu as branch_menu
from .menus.book_stocks import menu as book_stock_menu
from .menus.users import menu as user_menu
from .menus.transactions import menu as book_sales_menu

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
            book_sales_menu(connection)
        elif choice == 7:
            break
        else:
            print("Pilihan tidak valid")