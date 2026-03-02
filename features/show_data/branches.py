import pandas as pd

from db.queries import branches as br

def show_branch_data(connection):
    try:
        df = pd.read_sql(br.get_branches(), connection)

        print("\n=== DATA CABANG ===\n")

        if len(df) == 0:
            print("Tidak ada data yang tersedia")
        else:
            print(df)

        return df
    except Exception as e:
        print(f"Terjadi error saat menampilkan data: {e}")
        return None