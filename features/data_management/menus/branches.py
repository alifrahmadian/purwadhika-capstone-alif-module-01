from ..branches import add_branch

def menu(connection):
    while True:
        print("\n=== DATA CABANG ===")
        print("1. Tambah cabang")
        print("2. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-2): "))

        if choice == 1:
            add_branch(connection)
        elif choice == 2:
            break
        else:
            print("Pilihan tidak valid")