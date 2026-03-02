import mysql.connector

from features.show_data import genres as gd
from db.queries import (
    book_genres as bgq,
    books as bq
    )


def add_book(connection):
    run_input_genre = True

    cursor = connection.cursor()

    try:
        name = input("Masukkan nama buku: ")
        price = float(input("Masukkan harga buku: "))
        author = input("Masukkan nama penulis buku: ")
        reserved_stock = int(input("Masukkan jumlah stok yang dapat dialokasikan ke cabang-cabang: "))

        while run_input_genre:
            genre_data = gd.show_genre_data(connection)
            genre_id = int(input("Masukkan ID genre: "))

            existing_genre = bgq.get_genre_by_id(cursor, genre_id)
            if existing_genre is None:
                print("\n Genre tidak tersedia")
            else:
                run_input_genre = False
        
        existing_book = bq.get_book_by_name(cursor, name)
        if existing_book is not None:
            print("\n Buku sudah tersedia")
            return
        
        bq.add_book(cursor, name, price, author, reserved_stock, genre_id)
        connection.commit()

        print(f"\nBuku dengan judul {name.title()} berhasil ditambahkan")
    except mysql.connector.Error as e:
        print(f"Terjadi error saat menambahkan data: {e}")
        return None