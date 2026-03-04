import mysql.connector

from constants.cities import Cities as c
from constants.provinces import Provinces as p

from db.queries import branches as brq

def add_branch(connection):
    run_input_name = True
    run_input_address = True
    run_input_city = True
    run_input_province = True

    cursor = connection.cursor()

    try:
        while run_input_name:
            name = input("Masukkan nama cabang: ")

            existing_branch = brq.get_branch_by_name(cursor, name)

            if existing_branch is not None:
                print("\n Cabang sudah tersedia")
            else:
                run_input_name = False

        while run_input_address:
            address = input("Masukkan alamat cabang: ")

            existing_address = brq.get_branch_by_address(cursor, address)

            if existing_address is not None:
                print("\n Alamat sudah dipakai di cabang lain")
            else:
                run_input_address = False
        
        while run_input_city:
            city = choose_city()
            if city is None:
                print("Pilihan kota tidak sesuai")
            else:
                run_input_city = False

        while run_input_province:
            province = choose_province()
            if province is None:
                print("Pilihan provinsi tidak sesuai")
            else:
                run_input_province = False
        
        brq.add_branch(cursor, name, address, city.value, province.value)
        connection.commit()

        print(f"\n Cabang {name.title()} dengan alamat {address.title()} berhasil ditambahkan")
    except mysql.connector.Error as e:
        print(f"Terjadi error saat menambahkan data: {e}")
        return None

def choose_city():
    print("""Pilih kota pada cabang yang ingin ditambahkan: 
          1. Jakarta Selatan
          2. Jakarta Pusat
          3. Jakarta Barat
          4. Jakarta Timur
          5. Jakarta Utara
          6. Palembang
          7. Kota Bogor
          8. Kota Bekasi
          9. Depok
          10. Kabupaten Bekasi
          11. Kabupaten Bogor
          12. Kota Bandung
          13. Kota Tangerang
          14. Tangerang Selatan
          15. Kabupaten Tangerang
          16. Yogyakarta
          17. Kabupaten Sleman
          18. Surabaya
          19. Denpasar
          20. Medan
          21. Solo
          """)
    
    choice = input("Masukkan pilihan (1-21): ")

    mapping = {
        "1": c.JAKARTA_SELATAN,
        "2": c.JAKARTA_PUSAT,
        "3": c.JAKARTA_BARAT,
        "4": c.JAKARTA_TIMUR,
        "5": c.JAKARTA_UTARA,
        "6": c.PALEMBANG,
        "7": c.KOTA_BOGOR,
        "8": c.KOTA_BEKASI,
        "9": c.DEPOK,
        "10": c.KABUPATEN_BEKASI,
        "11": c.KABUPATEN_BOGOR,
        "12": c.KOTA_BANDUNG,
        "13": c.KOTA_TANGERANG,
        "14": c.TANGERANG_SELATAN,
        "15": c.KABUPATEN_TANGERANG,
        "16": c.YOGYAKARTA,
        "17": c.KABUPATEN_SLEMAN,
        "18": c.SURABAYA,
        "19": c.DENPASAR,
        "20": c.MEDAN,
        "21": c.SURAKARTA
    }
    
    return mapping.get(choice)

    
def choose_province():
    print("""Pilih provinsi pada cabang yang ingin ditambahkan: 
        1. DKI Jakarta
        2. Sumatera Selatan
        3. Jakarta Barat
        4. Banten
        5. Jawa Tengah
        6. DI Yogyakarta
        7. Jawa Timur
        8. Bali
        9. Sumatera Selatan
        """)

    choice = input("Masukkan pilihan (1-9): ")

    mapping = {
        "1": p.DKI_JAKARTA,
        "2": p.SUMATERA_SELATAN,
        "3": p.JAWA_BARAT,
        "4": p.BANTEN,
        "5": p.JAWA_TENGAH,
        "6": p.DI_YOGYAKARTA,
        "7": p.JAWA_TIMUR,
        "8": p.BALI,
        "9": p.SUMATERA_UTARA
    }

    return mapping.get(choice)