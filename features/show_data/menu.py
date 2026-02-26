import pandas as pd
import mysql.connector

from db.queries import (
    book_genres as bg, books as b, branches as br, book_stocks as bs, users as u
)
    

def show_data_menu(connection):
    while True:
        print("\n=== MENU TAMPILKAN DATA ===\n")
        print("Silakan pilih data yang ingin ditampilkan (1-7): \n")
        print("1. Data genre buku")
        print("2. Data buku")
        print("3. Data cabang")
        print("4. Data stok buku")
        print("5. Data penjualan")
        print("6. Data member")
        print("7. Kembali ke menu utama")
    
        choice = int(input("Masukkan pilihan anda: "))

        if choice == 1:
            show_genre_data(connection)
        elif choice == 2:
            show_book_data(connection)
        elif choice == 3:
            show_branch_data(connection)
        elif choice == 4:
            show_book_stock_data(connection)
        elif choice == 5:
            show_sales_data(connection)
        elif choice == 6:
            show_member_data(connection)
        elif choice == 7:
            break
        else:
            print("Pilihan tidak valid")

def show_genre_data(connection):
    try:
        df = pd.read_sql(bg.get_book_genres(), connection)

        print("\n=== DATA GENRE BUKU ===\n")
        print(df)
        return(df)
    except Exception as e:
        print(f"Terjadi error saat menampilkan data: {e}")
        return None

def show_book_data(connection):
    try:
        df = pd.read_sql(b.get_books(), connection)

        print("\n=== DATA BUKU ===")

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

def show_branch_data(connection):
    try:
        df = pd.read_sql(br.get_branches(), connection)

        print("\n=== DATA CABANG ===\n")
        print(df)
        return df
    except Exception as e:
        print(f"Terjadi error saat menampilkan data: {e}")
        return None

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

def show_sales_data(connection):
    pass

def show_member_data(connection):
    try:
        df = pd.read_sql(u.get_users(), connection)

        print("\n === DATA MEMBER === \n")

        if len(df) == 0:
            print("Tidak ada data yang tersedia")
        else:
            print(df)
        
        return df
    except:
        print(f"Terjadi error pada saat menampilkan data: {e}")
        return None

