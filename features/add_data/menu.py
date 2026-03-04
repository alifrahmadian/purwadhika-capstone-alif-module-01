from .genres import add_genre
from .books import add_book
from .branches import add_branch

def menu(connection):
    while True:
        print("\n=== MENU TAMBAH DATA ===")
        print("1. Tambah genre")
        print("2. Tambah buku")
        print("3. Tambah cabang")
        print("4. Tambah stok buku per cabang")
        print("5. Tambah user/member")
        print("6. Lakukan transaksi buku")
        print("7. Kembali ke menu utama")

        choice = int(input("Masukkan pilihan anda (1-7): "))

        if choice == 1:
            add_genre(connection)
        elif choice == 2:
            add_book(connection)
        elif choice == 3:
            add_branch(connection)
        elif choice == 4:
            print("Tambah stok buku per cabang")
        elif choice == 5:
            print("Tambah user/member")
        elif choice == 6:
            print("Transaksi")
        elif choice == 7:
            break
        else:
            print("Pilihan tidak valid")