import pandas as pd

from .genres import show_genre_data
from .books import show_book_data
from .branches import show_branch_data
from .book_stocks import show_book_stock_data
from .book_sales import show_sales_data
from .users import show_member_data

def menu(connection):
    while True:
        print("\n=== MENU TAMPILKAN DATA ===\n")
        print("Silakan pilih data yang ingin ditampilkan (1-7): \n")
        print("1. Data genre buku")
        print("2. Data buku")
        print("3. Data cabang")
        print("4. Data stok buku")
        print("5. Data penjualan")
        print("6. Data member")
        print("7. Kembali ke menu utama")
    
        choice = int(input("Masukkan pilihan anda: "))

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