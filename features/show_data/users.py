import pandas as pd

from db.queries import users as u

def show_member_data(connection):
    try:
        df = pd.read_sql(u.get_users(), connection)

        print("\n === DATA MEMBER === \n")

        if len(df) == 0:
            print("Tidak ada data yang tersedia")
        else:
            print(df)
        
        return df
    except Exception as e:
        print(f"Terjadi error pada saat menampilkan data: {e}")
        return None