from db.connection import create_connection

from features.show_data.menu import menu as show_data_menu
from features.data_management.main_menu import menu as data_management_menu
from features.data_visualization.main_menu import menu as visualize_data_menu
from features.show_mean.main_menu import menu as show_mean_menu

def main():
    connection = create_connection()

    while True:
        print("\n=== MENU UTAMA ===\n")
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
            data_management_menu(connection)
        elif choice == 3:
            pass
            show_mean_menu(connection)
        elif choice == 4:
            visualize_data_menu(connection)
        elif choice == 5:
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid")


if __name__ == '__main__':
    main()
