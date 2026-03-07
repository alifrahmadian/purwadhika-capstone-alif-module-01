from ..book_stocks import(
    add_book_stock,
    add_book_stock_amount_by_branch
)

def menu(connection):
     while True:
        print("\n=== DATA STOK BUKU ===")
        print("1. Daftar stok buku per cabang")
        print("2. Tambah jumlah stok buku per cabang")
        print("3. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-3): "))

        if choice == 1:
            add_book_stock(connection)
        elif choice == 2:
            add_book_stock_amount_by_branch(connection)
        elif choice == 3:
            break
        else:
            print("Pilihan tidak valid")