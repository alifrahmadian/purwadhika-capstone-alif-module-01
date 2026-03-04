import mysql.connector

def add_book_stock(connection):
    """
    Fungsi ini untuk menambahkan stok buku di setiap cabangnya (cabang yang terpilih). Fungsi ini berlaku untuk buku yang belum pernah tersedia di suatu cabang. Jika sudah tersedia, refer ke fungsi update_book_stock_by_branch.

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
        - Jika tersedia, return dan print "buku sudah tersedia di database untuk cabang ini" meskipun stoknya 0 -> karena ini akan dihandle oleh fungsi update_book_stock_by_branch
        - Jika tidak tersedia, lanjut ke tahap selanjutnya
    6. Masukkan jumlah buku yang ingin dijual pada cabang tersebut
    7. Cek tabel books, terutama kolom reserved_stock untuk buku tersebut
        - Jika stok yang ingin dijual melebihi reserved_stock, return dan print "Jumlah stok yang ingin dijual melebih stok yang tersedia"
        - Jika stok yang ingin dijual tidak melebihi reserved_stock, lanjut ke tahap selanjutnya
    8. Lakukan insert ke tabel book_stocks
    9. Kurangi reserved_stock pada buku tersebut di tabel books
    10. Tahap 8-9, lakukan SQL transaction
"""
            
    try:
        pass
    except mysql.connector.Error as e:
        print(f"Terjadi error saat menambahkan data: {e}")
        return None

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