from ..book_sales import create_transaction

def menu(connection):
    while True:
        print("\n=== DATA TRANSAKSI ===")
        print("1. Lakukan transaksi")
        print("2. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-2): "))

        if choice == 1:
            create_transaction(connection)
        elif choice == 2:
            break
        else:
            print("Pilihan tidak valid")