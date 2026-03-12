from features.data_visualization.book_sales import(
    visualize_book_sales,
    visualize_revenue_by_books,
    visualize_point_redemption_by_books,
    visualize_member_distribution,
    visualize_sales_trend_per_year
)

def menu(connection):
    while True:
        print("\n=== DATA PENJUALAN BUKU ===")
        print("1. Jumlah Penjualan Buku")
        print("2. Jumlah Pendapatan dari Penjualan Buku")
        print("3. Jumlah Point Redemption dari Penjualan Buku")
        print("4. Distribusi member yang pernah melakukan transaksi")
        print("5. Tren Penjualan per tahun")
        print("6. Kembali ke menu sebelumnya")

        choice = int(input("Masukkan pilihan anda (1-7): "))

        if choice == 1:
            visualize_book_sales(connection)
        elif choice == 2:
            visualize_revenue_by_books(connection)
        elif choice == 3:
            visualize_point_redemption_by_books(connection)
        elif choice == 4:
            visualize_member_distribution(connection)
        elif choice == 5:
            visualize_sales_trend_per_year(connection)
        elif choice == 6:
            break
        else:
            print("Pilihan tidak valid")