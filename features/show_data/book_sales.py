import pandas as pd

from db.queries import book_sales as bsl

def show_sales_data(connection):
    try:
        df = pd.read_sql(bsl.get_book_sales(), connection)

        print("\n === DATA PENJUALAN BUKU === \n")

        if len(df) == 0:
            print("Tidak ada data yang tersedia")
        else:
            print(df)
        
        return df
    except Exception as e:
        print(f"Terjadi error pada saat menampilkan data: {e}")
        return None