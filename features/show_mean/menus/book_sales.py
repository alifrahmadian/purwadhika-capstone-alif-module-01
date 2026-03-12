from features.show_mean.book_sales import (
    show_sales_summary,
    show_best_selling_books,
    show_top_branches,
    show_monthly_sales_trend,
    show_payment_method_stats
)

def menu(connection):
    while True:
        print("""
=== STATISTIK PENJUALAN ===
1. Ringkasan Penjualan
2. 10 Buku Terlaris
3. Cabang Penjualan Tertinggi
4. Tren Penjualan Bulanan
5. Metode Pembayaran Terpopuler
6. Kembali
""")
        choice = input("Masukkan pilihan anda (1-6): ")

        if choice == "1":
            show_sales_summary(connection)
        elif choice == "2":
            show_best_selling_books(connection)
        elif choice == "3":
            show_top_branches(connection)
        elif choice == "4":
            try:
                year = int(input("Masukkan tahun: "))
                show_monthly_sales_trend(connection, year)
            except ValueError:
                print("Tahun harus berupa angka.")
        elif choice == "5":
            show_payment_method_stats(connection)
        elif choice == "6":
            break
        else:
            print("Pilihan tidak valid")