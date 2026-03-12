def get_book_sales():
    return """
    SELECT bs.transaction_date, quantity, sales, redeemed_points, payment_method, u.name as user_name, u.phone_number, b.genre_id, b.name as book_name, b.price, b.author, br.name as branch FROM book_sales bs
    LEFT JOIN users u
        ON bs.user_id = u.id
    JOIN books b
        ON bs.book_id = b.id
    JOIN branches br
        ON bs.branch_id = br.id;
"""

def add_book_sales(cursor, transactions:list):
    query = """
    INSERT INTO book_sales (user_id, book_id, branch_id, transaction_date, quantity, sales, redeemed_points, payment_method)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""
    cursor.executemany(query, transactions)