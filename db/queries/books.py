def get_books():
    return """
    SELECT b.id, b.name, b.price, b.author, b.reserved_stock, bg.name as genre, bg.type from BOOKS b
    JOIN book_genres bg
    ON b.genre_id = bg.id;
"""