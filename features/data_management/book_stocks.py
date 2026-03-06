import mysql.connector

from db.queries import books as bq
from db.queries import branches as brq
from db.queries import book_stocks as bsq

from features.show_data.books import show_book_data
from features.show_data.branches import show_branch_data

def add_book_stock(connection):
    """
    Fungsi ini untuk menambahkan stok buku di setiap cabangnya (cabang yang terpilih). Fungsi ini berlaku untuk buku yang belum pernah tersedia di suatu cabang. Jika sudah tersedia, refer ke fungsi `update_book_stock_by_branch()`.
"""
    run_input_book = True
    run_input_branch = True
    run_input_stock = True
    reserved_stock = 0
    book_id = 0

    cursor = connection.cursor()

    try:
        while run_input_book:
            show_book_data(connection)

            book_name = input("Masukkan nama buku yang ingin dimasukkan ke dalam stok: ")

            if book_name == "":
                print("Nama buku tidak boleh kosong")
            else:
                try:
                    existing_book = bq.get_book_by_name(cursor, book_name)
                    if existing_book is None:
                        print(f"\nBuku {book_name.title()} tidak tersedia di database")
                    else:
                        reserved_stock = existing_book[5]
                        book_id = existing_book[0]

                        run_input_book = False
                except mysql.connector.Error as e:
                    print(f"Terjadi error: {e}")
                    break
        
        print(f"Reserved Stock: {reserved_stock}")
        print(f"Book ID: {book_id}")
    
        while run_input_branch:
            show_branch_data(connection)

            branch_id = int(input("Masukkan ID cabang: "))

            existing_branch = brq.get_branch_by_id(cursor, branch_id)

            if existing_branch is None:
                print(f"\nCabang dengan ID {branch_id} tidak ditemukan")
            else:
                run_input_branch = False
        
        book_availability = bsq.get_book_stock_by_name_and_branch(cursor, book_name, branch_id)

        if book_availability is not None:
            print("\nBuku sudah tersedia di cabang ini berdasarkan database kami. Silakan menuju ke menu perbarui stok jika anda ingin memperbarui stok buku ini.")
            return 

        while run_input_stock:
            book_stocks = int(input("Masukkan jumlah stok buku yang ingin dijual: "))

            if book_stocks > reserved_stock:
                print(f"Stok buku {book_name} yang anda masukkan melebihi jumlah stok yang tersedia di gudang. Jumlah stok buku yang tersedia adalah {reserved_stock}")
            else:
                run_input_stock = False

        bsq.add_book_stock(cursor, book_id, branch_id, book_stocks)

        updated_reserved_stocks = reserved_stock - book_stocks
        
        bq.update_reserved_stock(cursor, book_id, updated_reserved_stocks)

        connection.commit()

        print(f"Stok buku {book_name} berhasil ditambahkan sebanyak {book_stocks} buah")
    except mysql.connector.Error as e:
        connection.rollback()

        print(f"Terjadi error saat menambahkan data: {e}")
        return None
    finally:
        cursor.close()

def update_book_stock_by_branch(connection):
    """
        Fungsi ini untuk memperbarui stok buku yang terjual di cabang tersebut.

        Logic:
            1. Input nama buku
            2. Cek apakah buku tersebut tersedia di database buku. 
                - Jika buku tersebut tidak tersedia di tabel books, user input ulang
                - Jika buku tersebut tersedia di tabel books, lanjut ke tahap selanjutnya
            3. Input id cabang
            4. Cek apakah cabang yang di-input oleh user valid.
                - Jika tidak valid, user input ulang
                - Jika valid, lanjut ke tahap selanjutnya
            5. Cek apakah buku sudah tersedia di tabel book_stocks.
                - Jika tidak tersedia, return dan print "buku tidak tersedia di cabang ini" 
                - Jika tersedia, lanjut ke tahap selanjutnya
            6. Masukkan jumlah buku yang ingin di-update pada cabang tersebut
            7. Cek tabel books, terutama kolom reserved_stock untuk buku tersebut
                - Jika stok yang ingin dijual melebihi reserved_stock, return dan print "Jumlah stok yang ingin dijual melebih stok yang tersedia"
                - Jika stok yang ingin dijual tidak melebihi reserved_stock, lanjut ke tahap selanjutnya
            8. Lakukan update pada kolom stock di tabel book_stocks
            9. Kurangi reserved_stock pada buku tersebut di tabel books
            10. Tahap 8-9, lakukan SQL transaction
    """
    pass