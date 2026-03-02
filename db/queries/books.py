def get_books():
    return """
    SELECT b.id, b.name, b.price, b.author, b.reserved_stock, bg.name as genre, bg.type from BOOKS b
    JOIN book_genres bg
    ON b.genre_id = bg.id;
"""

def get_book_by_name(cursor, name:str):
    query = """
    SELECT * from books
    WHERE name = %s
    LIMIT 1;
"""

    cursor.execute(query, (name, ))
    return cursor.fetchone()

def add_book(cursor, name: str, price: float, author: str, reserved_stock: int, genre_id: int):
    query = """
        INSERT INTO books (name, price, author, reserved_stock, genre_id)
        VALUES(%s, %s, %s, %s, %s);
"""

    values = (name.title(), price, author.title(), reserved_stock, genre_id)
    cursor.execute(query, values)