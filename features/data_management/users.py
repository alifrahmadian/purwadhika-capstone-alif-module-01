import mysql.connector

from db.queries import users as uq
from utils import user_input_validation as userval

def add_user(connection):
    run_input_email = True
    run_input_phone_number = True

    cursor = connection.cursor()

    try:
        name = input("Masukkan nama pelanggan: ")

        while run_input_email:
            email = input("Masukkan email: ")

            is_valid_email = userval.is_valid_email(email)
            if not is_valid_email:
                print("\nFormat email tidak valid")

            email_exist = uq.get_user_by_email(cursor, email)
            if email_exist is not None:
                print("\nEmail ini sudah terdaftar")

            if is_valid_email and email_exist is None:
                run_input_email = False
        
        while run_input_phone_number:
            phone_number = input("Masukkan nomor telepon: ")

            is_valid_phone_number = userval.is_valid_phone_number(phone_number)
            if not is_valid_phone_number:
                print("\nFormat nomor telepon tidak sesuai")
            
            phone_number_exist = uq.get_user_by_phone_number(cursor, phone_number)
            if phone_number_exist is not None:
                print("\nNomor telepon ini sudah terdaftar")
            
            if is_valid_phone_number and phone_number_exist is None:
                run_input_phone_number = False
        
        uq.add_user(cursor, name, email, phone_number)
        connection.commit()

        print(f"\nUser dengan nama {name.title()} berhasil terdaftar")
    except mysql.connector.Error as e:
        print(f"Terjadi error saat menambahkan data: {e}")
        return None
    finally:
        cursor.close()

