from ..books import add_book

def menu(connection):
    while True:
        print("\n=== DATA BUKU ===")
        print("1. Tambah buku")
        print("2. Update harga buku")
        print("3. Tambah stok buku yang bisa disebarkan ke cabang (reserved)")
        print("4. Ubah nama buku")
        print("5. Ubah nama penulis buku")
        print("6. Ubah genre buku")
        print("7. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-7): "))

        if choice == 1:
            add_book(connection)
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            break
        else:
            print("Pilihan tidak valid")