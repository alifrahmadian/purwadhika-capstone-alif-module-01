import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector

from db.connection import create_connection
from features.show_data.menu import show_data_menu

def add_data_menu():
    print("Tambah data")

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
        print("2. Tambah data baru")
        print("3. Tampilkan rata-rata")
        print("4. Tampilkan visualisasi data")
        print("5. Keluar")

        choice = int(input("Masukkan pilihan anda dengan memasukkan angka 1-5: "))

        if choice == 1:
            show_data_menu(connection)
        elif choice == 2:
            add_data_menu()
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
