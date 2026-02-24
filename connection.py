import mysql.connector
from dotenv import load_dotenv
import os

def create_connection():
    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_database = os.getenv("DB_DATABASE")


    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database,
        )

        print("Koneksi ke database berhasil")
        return connection
    except mysql.connector.Error as e:
        print(f"Terjadi error pada koneksi database: {e}")
        return None