import mysql.connector
from datetime import date

from utils import user_input_validation as userval
from utils import dataframe as dfutil
from utils import user_tier as tierutil

from features.show_data.branches import show_branch_data
from features.show_data.books import show_book_data

from db.queries import users as uq
from db.queries import branches as brq
from db.queries import books as bq
from db.queries import book_stocks as bsq
from db.queries import book_sales as sq

from constants.payment_methods import PaymentMethods as pm

def create_transaction(connection):
    shopping_lists = [] # book id, book name, quantity, price, point_per_item -> untuk menampilkan list belanjaan

    transactions = [] # di list inilah yang akan ditambahkan ke tabel book_stocks

    input_branch_id_run = True
    input_member_run = True

    input_phone_number_run = True
    input_email_run = True
    input_user_id_run = True

    input_payment_method_run = True

    grand_total = 0
    payment_amount = 0
    change_money = 0

    user = None
    payment_method = None

    transaction_date = date.today()

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
                            continue
                        
                        user = uq.get_user_by_phone_number(cursor, phone_number)
                        if user is None:
                            print("\nMember belum terdaftar")
                            continue
                        else:
                            input_phone_number_run = False
                            input_member_run = False

                elif member_input == 2:
                    while input_email_run:
                        email = input("Masukkan email: ")

                        is_valid_email = userval.is_valid_email(email)
                        if not is_valid_email:
                            print("\nFormat email tidak sesuai")
                            continue
                        
                        user = uq.get_user_by_email(cursor, email)
                        if user is None:
                            print("\nMember belum terdaftar")
                            continue
                        else:
                            input_email_run = False
                            input_member_run = False
                else:
                    while input_user_id_run:
                        user_id = int(input("Masukkan ID user: "))

                        user = uq.get_user_by_id(cursor, user_id)
                        if user is None:
                            print("\nMember belum terdaftar")
                            continue
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
                book_df = show_book_data(connection)
                print(book_df)

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
            point_per_item = tierutil.convert_price_to_points(float(total_item_price))
            shopping_list = (book_id, book_name, qty, book_price, point_per_item, total_item_price)

            shopping_lists.append(shopping_list)

        
        shopping_lists_df = dfutil.convert_list_to_dataframe(shopping_lists, ['book_id', 'book_name', 'quantity', 'book_price','point_per_item', 'total_price'])

        grand_total = float(shopping_lists_df['total_price'].sum())
        grand_total_point = tierutil.convert_price_to_points(grand_total)
        print("\n=== DAFTAR BELANJA===\n")
        print(shopping_lists_df)

        print(f"\nTotal harga: Rp{grand_total:.0f}")
        print(f"Jumlah point yang bisa di-redeem: {grand_total_point}")

        if user is not None:
            print(f"Jumlah point yang dimiliki oleh pelanggan ini adalah {points}")
        
        while input_payment_method_run:
            payment_method  = choose_payment_method()

            if payment_method is None:
                print("\nPilihan metode pembayaran tidak valid")
                continue
            
            """
            Validasi untuk metode pembayaran point redemption
            """
            if payment_method == pm.PAYMENT_METHOD_POINT_REDEMPTION and user is None:
                print("\nPelanggan ini tidak memiliki member, sehingga tidak bisa menggunakan metode pembayaran point redemption")
                continue
            elif payment_method == pm.PAYMENT_METHOD_POINT_REDEMPTION and points < grand_total_point:
                print("\nJumlah point pelanggan tidak mencukupi untuk melakukan pembayaran menggunakan metode point redemption")
                continue
            else:                
                input_payment_method_run = False

            if payment_method == pm.PAYMENT_METHOD_CASH:
                while True:
                    payment_amount = float(input("Masukkan jumlah uang yang dibayarkan oleh pelanggan: "))
                    if payment_amount < grand_total:
                        print("\nJumlah uang yang dibayarkan tidak mencukupi untuk membayar total harga belanjaan")
                        continue
                    else:
                        change_money = payment_amount - grand_total
                        break

            if payment_method in [pm.PAYMENT_METHOD_DEBIT_CARD, pm.PAYMENT_METHOD_CREDIT_CARD, pm.PAYMENT_METHOD_EWALLET, pm.PAYMENT_METHOD_QRIS]:
                while True:
                    payment_amount = float(input("Masukkan jumlah uang yang dibayarkan oleh pelanggan: ")
                    )
                    if payment_amount > grand_total:
                        print(f"\nUang yang dibayarkan melebihi total harga belanjaan")
                        continue
                    elif payment_amount < grand_total:
                        print(f"\nUang yang dibayarkan tidak mencukupi untuk membayar total harga belanjaan")
                        continue
                    else:  
                        input_payment_method_run = False
                        break
    
        transactions = [
            (
                user_id if user is not None else None,
                book_id,
                branch_id,
                transaction_date,
                qty,
                total_item_price if payment_method != pm.PAYMENT_METHOD_POINT_REDEMPTION else 0,
                point_per_item if payment_method == pm.PAYMENT_METHOD_POINT_REDEMPTION else 0,
                payment_method.value
            )
            for book_id, book_name, qty, total_item_price, point_per_item, grand_total in shopping_lists
        ]

        sq.add_book_sales(cursor, transactions)

        for book_id, book_name, qty, total_item_price, point_per_item, grand_total in shopping_lists:
            updated_stock = available_stock - qty

            bsq.update_book_stock_by_book_and_branch(cursor, book_id, branch_id, updated_stock)
        
        if user is not None:
            if payment_method == pm.PAYMENT_METHOD_POINT_REDEMPTION:
                updated_points = points - grand_total_point
                uq.update_user_points(cursor, user_id, updated_points) 
            else:
                updated_points = points + grand_total_point
                uq.update_user_points(cursor, user_id, updated_points)
        
        connection.commit()
        print("\nTransaksi berhasil!")

        if payment_method == pm.PAYMENT_METHOD_CASH:
            print(f"Uang yang dibayarkan: Rp{payment_amount:.0f}")
            print(f"Kembalian: Rp{change_money:.0f}")
        
        if payment_method == pm.PAYMENT_METHOD_POINT_REDEMPTION:
            print(f"Point yang diredeem: {grand_total_point:.0f}")
            print(f"Point yang dimiliki setelah transaksi: {updated_points:.0f}")
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

def choose_payment_method():
    print("Pilih metode pembayaran: ")
    print("1. Cash")
    print("2. Kartu Debit")
    print("3. Kartu Kredit")
    print("4. E-wallet")
    print("5. QRIS")
    print("6. Point Redemption")

    choice = input("Masukkan pilihan anda (1-6): ")
    mapping = {
        "1": pm.PAYMENT_METHOD_CASH,
        "2": pm.PAYMENT_METHOD_DEBIT_CARD,
        "3": pm.PAYMENT_METHOD_CREDIT_CARD,
        "4": pm.PAYMENT_METHOD_EWALLET,
        "5": pm.PAYMENT_METHOD_QRIS,
        "6": pm.PAYMENT_METHOD_POINT_REDEMPTION
    }

    return mapping.get(choice)