import pandas as pd

from db.queries import book_genres as bg

def show_genre_data(connection):
    try:
        df = pd.read_sql(bg.get_book_genres(), connection)

        print("\n=== DATA GENRE BUKU ===\n")

        if len(df) == 0:
            print("Tidak ada data yang tersedia")
        else:
            print(df)

        return df
    except Exception as e:
        print(f"Terjadi error saat menampilkan data: {e}")
        return None