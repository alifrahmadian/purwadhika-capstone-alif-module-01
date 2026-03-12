from .menus.book_sales import menu as book_sales_menu

def menu(connection):
    while True:
        print("\n === STATISTIK ===")
        print("1. Data penjualan buku")
        print("2. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-2): "))

        if choice == 1:
            book_sales_menu(connection)
        elif choice == 2:
            break
        else:
            print("Pilihan tidak valid")