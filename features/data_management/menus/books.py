from ..books import add_book

def menu(connection):
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