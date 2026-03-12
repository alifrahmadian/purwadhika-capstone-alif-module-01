from ..users import add_user

def menu(connection):
    while True:
        print("\n === DATA USER === ")
        print("1. Tambah data user")
        print("2. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-2): "))

        if choice == 1:
            add_user(connection)
        elif choice == 2:
            break
        else:
            print("Pilihan tidak valid")