import pandas as pd

from db.queries import books as b

def show_book_data(connection):
    try:
        df = pd.read_sql(b.get_books(), connection)

        print("\n=== DATA BUKU ===")

        if len(df) == 0:
            print("Tidak ada data yang tersedia")
        else:
            renamed = df.rename(columns={
                'id': 'Book ID',
                'price': 'Price(Rp)',
                'name': 'Book Name',
                'author': 'Author',
                'genre': 'Genre',
                'type': 'Genre Type',
                'reserved_stock': 'Reserved Stock'
                })

            print(renamed)

        return renamed
    except Exception as e:
        print(f"Terjadi error saat menampilkan data: {e}")
        return None