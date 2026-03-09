import mysql.connector

from utils import user_input_validation as userval
from utils import dataframe as dfutil
from utils import user_tier as tierutil

from features.show_data.branches import show_branch_data
from features.show_data.books import show_book_data

from db.queries import users as uq
from db.queries import branches as brq
from db.queries import books as bq
from db.queries import book_stocks as bsq

def create_transaction(connection):
    shopping_lists = [] # book id, book name, quantity, price -> untuk menampilkan list belanjaan

    transactions = [] # di list inilah yang akan ditambahkan ke tabel book_stocks

    input_branch_id_run = True
    input_member_run = True

    input_phone_number_run = True
    input_email_run = True
    input_user_id_run = True

    grand_total = 0

    user = None

    cursor = connection.cursor()

    try:
        while input_branch_id_run:
            branch_data = show_branch_data(connection)
            print(branch_data)

            branch_id = int(input("Masukkan ID cabang: "))

            branch = brq.get_branch_by_id(cursor, branch_id)
            if branch is None:
                print("\nID cabang tidak tersedia")
            else:
                input_branch_id_run = False


        while input_member_run:
            check_member = input("Apakah pelanggan memiliki member [ya|tidak]? ").lower()
            if check_member == 'tidak':
                input_member_run = False
                
            else:
                member_input = member_input_choice()

                if member_input == 1:
                    while input_phone_number_run:
                        phone_number = input("Masukkan nomor telepon: ")

                        is_valid_phone_number = userval.is_valid_phone_number(phone_number)
                        if not is_valid_phone_number:
                            print("\nFormat nomor telepon tidak sesuai")
                        
                        user = uq.get_user_by_phone_number(cursor, phone_number)
                        if user is None:
                            print("\nMember belum terdaftar")
                            input_phone_number_run = False
                        else:
                            input_phone_number_run = False
                            input_member_run = False

                elif member_input == 2:
                    while input_email_run:
                        email = input("Masukkan email: ")

                        is_valid_email = userval.is_valid_email(email)
                        if not is_valid_email:
                            print("\nFormat email tidak sesuai")
                        
                        user = uq.get_user_by_email(cursor, email)
                        if user is None:
                            print("\nMember belum terdaftar")
                            input_email_run = False
                        else:
                            input_email_run = False
                            input_member_run = False
                else:
                    while input_user_id_run:
                        user_id = int(input("Masukkan ID user: "))

                        user = uq.get_user_by_id(cursor, user_id)
                        if user is None:
                            print("\nMember belum terdaftar")
                            input_user_id_run = False
                        else:
                            input_user_id_run = False
                            input_member_run = False

        if user is not None:
            user_id = user[0]
            name = user[1]
            phone_number = user[2]
            points = user[3]
            tier = user[4].capitalize()
            email = user[5]

            print(f"\nNama Pelanggan: {name}")
            print(f"ID: {user_id}")
            print(f"Nomor telepon: {phone_number}")
            print(f"Email: {email}")
            print(f"\nJumlah point: {points:.0f}")
            print(f"Keanggotaan: {tier}")

        num_of_items = int(input("\nBerapa jumlah item yang akan dibeli oleh pelanggan? "))

        for i in range(num_of_items):
            book = None
            book_stock = None

            book_name = ""
            book_price = 0
            available_stock = 0

            input_book_run = True
            input_qty_run = True

            while input_book_run:
                book_data = show_book_data(connection)
                print(book_data)

                book_id = int(input("Masukkan ID buku: "))
                book = bq.get_book_by_id(cursor, book_id)
                if book is None:
                    print(f"\nBuku dengan ID ini tidak tersedia")
                
                book_stock = bsq.get_book_stock_by_book_id_and_branch(cursor, book_id, branch_id)
                if book_stock is None:
                    print(f"\nBuku yang anda pilih tidak tersedia di cabang ini")
                
               

                if book is not None and book_stock is not None:
                    book_name = book[2]
                    book_price = book[3]
                    available_stock = book_stock[5]

                    input_book_run = False
            
            while input_qty_run:
                qty = int(input("Masukkan jumlah buku yang ingin dibeli: "))
                if qty > available_stock:
                    print("\nJumlah buku yang anda masukkan melebih jumlah buku yang tersedia di toko ini. ")
                else:
                    input_qty_run = False
            
            total_item_price = qty * book_price
            shopping_list = (book_id, book_name, qty, book_price, total_item_price)

            shopping_lists.append(shopping_list)

        
        shopping_lists_df = dfutil.convert_list_to_dataframe(shopping_lists, ['book_id', 'book_name', 'quantity', 'book_price', 'total_price'])

        grand_total = float(shopping_lists_df['total_price'].sum())
        grand_total_point = tierutil.convert_price_to_points(grand_total)
        print("\n=== DAFTAR BELANJA===\n")
        print(shopping_lists_df)

        print(f"\nTotal harga: Rp{grand_total:.0f}")
        print(f"Jumlah point yang bisa di-redeem: {grand_total_point}")
    except mysql.connector.Error as e:
        connection.rollback()

        print(f"Terjadi error saat menambahkan data: {e}")
        return None
    finally:
        cursor.close()

def member_input_choice():
    while True:
        print("\nMasukkan data member berdasarkan: ")
        print("1. Nomor telepon")
        print("2. Email")
        print("3. ID Customer")

        choice = int(input("Masukkan pilihan anda (1-3): "))

        if choice < 1 or choice > 3:
            print("Pilihan tidak sesuai")
        else:
            return choice
