import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector

from db.connection import create_connection
from features.show_data.menu import menu as show_data_menu
from features.data_management.menus import menu as add_data_menu

def show_mean_menu():
    print("Tampilkan rata-rata")

def visualize_data_menu():
    print("Tampilkan visualisasi data")

def main():
    connection = create_connection()

    while True:
        print("=== MENU UTAMA ===")
        print("\nSelamat Datang di Maxi Bookstore\n")
        print("1. Tampilkan data")
        print("2. Manajemen data")
        print("3. Tampilkan rata-rata")
        print("4. Visualisasi data")
        print("5. Keluar")

        choice = int(input("Masukkan pilihan anda (1-5): "))

        if choice == 1:
            show_data_menu(connection)
        elif choice == 2:
            add_data_menu(connection)
        elif choice == 3:
            show_mean_menu()
        elif choice == 4:
            visualize_data_menu()
        elif choice == 5:
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid")


if __name__ == '__main__':
    main()

"""
Fitur-fitur yang bisa diconsider (jika waktu pengerjaan sempat):

1. Menambah tabel member_point_transaction (id, user_id, book_sales_id, earned_points, point_expiry_date -> satu tahun setelah transaksi) -> tabel ini bertujuan untuk tracking riwayat point user setiap melakukan transaksi
    - Jika point expired, point user di tabel user akan berkurang dan berpotensi turun level tiernya

2. Fitur redeem point -> bayar menggunakan point
    - Apakah dimasukkan ke dalam tabel book_sales (amountnya) -> Atau karena redeem menggunakan point, amount transactionnya jadi 0?

3. Fitur di mana user dapat melakukan lebih dari satu transaksi di waktu yang sama (multiple books) 

Improvement (kalo sempat):
1. Tabel cities
2. Tabel provinces
3. Tabel tier, nanti di tabel user, instead of pake "tier", pake "tier_id"
"""
