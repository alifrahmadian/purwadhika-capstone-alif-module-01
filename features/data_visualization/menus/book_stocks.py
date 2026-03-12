from features.data_visualization.book_stocks import(
    visualize_book_stocks,
    visualize_book_stocks_by_branch,
    visualize_book_stocks_by_genre,
    visualize_book_stocks_by_genre_and_branch,
    visualize_book_stocks_by_genre_type,
    visualize_book_stocks_by_genre_type_and_branch,
    visualize_book_distribution,
    visualize_book_stock_distribution,
    visualize_book_stock_heatmap
)

def menu(connection):
    while True:
        print("\n === DATA STOK BUKU ===")
        print("1. Jumlah stok buku")
        print("2. Jumlah stok buku berdasarkan genre")
        print("3. Jumlah stok berdasarkan tipe genre")
        print("4. Distribusi Stok Buku")
        print("5. Distribusi Buku Yang Tersedia")
        print("6. Heatmap Stok Buku")
        print("7. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-7): "))

        if choice == 1:
            visualize_book_stocks(connection)
        elif choice == 2:
            visualize_book_stocks_by_genre(connection)
        elif choice == 3:
            visualize_book_stocks_by_genre_type(connection)
        elif choice == 4:
            visualize_book_stock_distribution(connection)
        elif choice == 5:
            visualize_book_distribution(connection)
        elif choice == 6:
            visualize_book_stock_heatmap(connection)
        elif choice == 7:
            break
        else:
            print("Pilihan tidak valid")