def get_book_genres():
    return "SELECT * FROM book_genres"

def add_genre(cursor, name: str, genre_type: str):
    query = """
        INSERT INTO book_genres (name, type)
        VALUES(%s, %s);
"""

    values = (name.title(), genre_type)
    cursor.execute(query, values)

def get_genre_by_name(cursor, name: str):
    query = """
        SELECT * from book_genres
        WHERE name = %s
        LIMIT 1;
"""

    cursor.execute(query, (name, ))
    return cursor.fetchone()

def get_genre_by_id(cursor, id: int):
    query = """
        SELECT * from book_genres
        WHERE id = %s
        LIMIT 1;
"""

    cursor.execute(query, (id, ))
    return cursor.fetchone()