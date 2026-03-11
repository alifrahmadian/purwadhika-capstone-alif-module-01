def get_book_stocks():
    return """
        SELECT 
            bs.id, b.name as book_name, b.price, b.author,
            br.name as branch, bs.stock, bg.name as genre_name, bg.type
        FROM book_stocks bs
        JOIN books b
            ON bs.book_id = b.id
        JOIN branches br
            ON bs.branch_id = br.id
        JOIN book_genres bg
            ON b.genre_id = bg.id;
    """

def get_book_stock_by_name_and_branch(cursor, book_name:str, branch_id:int):
    query = """
        SELECT 
            bs.id, b.name as book_name, b.price, b.author,
            br.name as branch, bs.stock 
        FROM book_stocks bs
        JOIN books b
            ON bs.book_id = b.id
        JOIN branches br
            ON bs.branch_id = br.id
        WHERE b.name = %s AND bs.branch_id = %s;
"""

    cursor.execute(query, (book_name, branch_id))
    return cursor.fetchone()

def get_book_stock_by_book_id_and_branch(cursor, book_id:int, branch_id:int):
    query = """
        SELECT 
            bs.id, b.name as book_name, b.price, b.author,
            br.name as branch, bs.stock 
        FROM book_stocks bs
        JOIN books b
            ON bs.book_id = b.id
        JOIN branches br
            ON bs.branch_id = br.id
        WHERE b.id = %s AND bs.branch_id = %s;
"""

    cursor.execute(query, (book_id, branch_id))
    return cursor.fetchone()

def get_book_stock_by_branch_id(cursor, id:int):
    query = """
    SELECT 
        bs.id, b.name as book_name, b.price, b.author,
        br.name as branch, bs.stock 
    FROM book_stocks bs
    JOIN books b
        ON bs.book_id = b.id
    JOIN branches br
        ON bs.branch_id = br.id
    WHERE bs.branch_id = %s;
"""

    cursor.execute(query, (id, ))
    return cursor.fetchall(), cursor.description

def add_book_stock(cursor, book_id:int, branch_id:int, stock: int):
    query = """
        INSERT INTO book_stocks (book_id, branch_id, stock)
        VALUES(%s, %s, %s);    
"""

    values = (book_id, branch_id, stock)
    cursor.execute(query, values)

def update_book_stock_by_book_and_branch(cursor, book_id:int, branch_id:int, stock:int):
    query = """
        UPDATE book_stocks
        SET stock = %s
        WHERE book_id = %s AND branch_id = %s;
"""

    values = (stock, book_id, branch_id)
    cursor.execute(query, values)