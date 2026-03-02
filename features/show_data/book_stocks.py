import pandas as pd

from db.queries import book_stocks as bs

def show_book_stock_data(connection):
    try:
        df = pd.read_sql(bs.get_book_stocks(), connection)
        
        print("\n === DATA STOK BUKU === \n")

        if len(df) == 0:
            print("Tidak ada data yang tersedia")
        else:
            print(df)

        return df
    except Exception as e:
        print(f"Terjadi error pada saat menampilkan data: {e}")
        return None