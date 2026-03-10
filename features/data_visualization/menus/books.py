from features.data_visualization.books import (
    visualize_reserved_stocks,
    visualize_reserved_stocks_by_genre,
    visualize_reserved_stocks_by_author,
    visualize_reserved_stocks_by_genre_type,
    visualize_book_price_distribution,
    visualize_book_reserved_stock_distribution
    )

def menu(connection):
    while True:
        print("\n === DATA BUKU ===")
        print("1. Jumlah reserved stock buku")
        print("2. Jumlah reserved stok buku per genre")
        print("3. Jumlah reserved stok buku berdasarkan penulis")
        print("4. Jumlah reserved stok buku berdasarkan tipe genre")
        print("5. Distribusi harga buku")
        print("6. Distribusi reserved stock")
        print("7. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-7): "))

        if choice == 1:
            visualize_reserved_stocks(connection)
        elif choice == 2:            
            visualize_reserved_stocks_by_genre(connection)
        elif choice == 3:
            visualize_reserved_stocks_by_author(connection)
        elif choice == 4:
            visualize_reserved_stocks_by_genre_type(connection)
        elif choice == 5:
            visualize_book_price_distribution(connection)
        elif choice == 6:
            visualize_book_reserved_stock_distribution(connection)
        elif choice == 7:
            break
        else:
            print("Pilihan tidak valid")

