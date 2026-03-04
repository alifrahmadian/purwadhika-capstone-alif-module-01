from constants.genre_type import GenreType as gt
from db.queries import book_genres as bgq

import mysql.connector

def add_genre(connection):
    try:
        name = input("Masukkan nama genre: ")
        genre_type = choose_genre_type()
        if genre_type is None:
            print("Pilihan genre tidak valid")
            return
        
        cursor = connection.cursor()

        existing_genre = bgq.get_genre_by_name(cursor, name)
        if existing_genre is not None:
            print(f"\nGenre buku {name.title()} sudah tersedia di database")
            return
        
        bgq.add_genre(cursor, name, genre_type.value)
        connection.commit()

        print(f"\nGenre {name.title()} berhasil ditambahkan")
    except mysql.connector.Error as e:
        print(f"Terjadi error saat menambahkan data: {e}")
        return None 

    
def choose_genre_type():
    print("Pilih tipe genre:")
    print("1. Fiction")
    print("2. Non-Fiction")

    choice = input("Masukkan pilihan (1-2): ")

    mapping = {
        "1": gt.FICTION,
        "2": gt.NON_FICTION
    }

    return mapping.get(choice)
    