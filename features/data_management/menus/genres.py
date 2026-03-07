from ..genres import add_genre

def menu(connection):
    while True:
        print("\n=== DATA GENRE ===")
        print("1. Tambah genre")
        print("2. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-2): "))

        if choice == 1:
            add_genre(connection)
        elif choice == 2:
            break
        else:
            print("Pilihan tidak valid")