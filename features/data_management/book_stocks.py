import mysql.connector

from db.queries import books as bq
from db.queries import branches as brq
from db.queries import book_stocks as bsq

from features.show_data.books import show_book_data
from features.show_data.branches import show_branch_data

from utils import dataframe as dfutil

def add_book_stock(connection):
    """
    Fungsi ini untuk mendaftarkan buku yang akan dijual di cabang yang dipilih.
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

        print(f"Stok buku {book_name.title()} berhasil ditambahkan sebanyak {book_stocks} buah")
    except mysql.connector.Error as e:
        connection.rollback()

        print(f"Terjadi error saat menambahkan data: {e}")
        return None
    finally:
        cursor.close()

def add_book_stock_amount_by_branch(connection):
    """
        Fungsi ini untuk menambahkan stok buku yang sudah terdaftar di cabang tersebut meskipun stoknya pada saat itu adalah 0.
    """

    run_input_book = True
    run_input_branch = True
    run_input_stock = True

    branch_id = 0
    current_stock = 0
    book_id = 0

    cursor = connection.cursor()

    try:
        while run_input_branch:
            show_branch_data(connection)

            branch_id = int(input("Masukkan ID cabang: "))

            existing_branch = brq.get_branch_by_id(cursor, branch_id)

            if existing_branch is None:
                print(f"\nCabang dengan ID {branch_id} tidak ditemukan")
            else:
                rows, description = bsq.get_book_stock_by_branch_id(cursor, branch_id)
                df = dfutil.convert_to_dataframe(rows, description)

                if len(df) == 0:
                    print("\nTidak ada buku yang tersedia di cabang ini")
                else:
                    print(f"\nBuku yang tersedia di cabang {rows[0][4]}: ")
                    print(df.to_string(index=False))
                    run_input_branch = False

        while run_input_book:
            book_name = input("Masukkan nama buku yang ingin ditambahkan stoknya: ")

            if book_name == "":
                print("Nama buku tidak boleh kosong")
            else:
                try:
                    book_availability = bsq.get_book_stock_by_name_and_branch(cursor, book_name, branch_id)

                    if book_availability is None:
                        print("\nBuku ini belum pernah didaftarkan di cabang ini")
                        return 
                    else:
                        current_stock = book_availability[5]
                        run_input_book = False
                except mysql.connector.Error as e:
                    print(f"Terjadi error: {e}")
                    break
        
        inputted_book = bq.get_book_by_name(cursor, book_name)
        reserved_stock = inputted_book[5]
        book_id = inputted_book[0]
        
        while run_input_stock:
            book_stocks = int(input("Masukkan jumlah stok buku yang ingin ditambahkan: "))

            if book_stocks > reserved_stock:
                print(f"Stok buku {book_name} yang anda masukkan melebihi jumlah stok yang tersedia di gudang. Jumlah stok buku yang tersedia adalah {reserved_stock}")
            else:
                run_input_stock = False

        new_stocks = current_stock + book_stocks
        bsq.update_book_stock_by_book_and_branch(cursor, book_id, branch_id, new_stocks)

        updated_reserved_stocks = reserved_stock - book_stocks
        bq.update_reserved_stock(cursor, book_id, updated_reserved_stocks)

        connection.commit()

        print(f"Stok buku {book_name.title()} berhasil ditambahkan sebanyak {book_stocks} buah")
    except mysql.connector.Error as e:
        connection.rollback()

        print(f"Terjadi error saat menambahkan data: {e}")
        return None
    finally:
        cursor.close()