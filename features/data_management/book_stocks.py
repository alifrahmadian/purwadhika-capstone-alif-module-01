import mysql.connector

def add_book_stock(connection):
    try:
        pass
    except mysql.connector.Error as e:
        print(f"Terjadi error saat menambahkan data: {e}")
        return None
