def get_book_sales():
    return """
    SELECT bs.transaction_date, quantity, sales, u.name as user_name, u.phone_number, b.genre_id, b.name as book_name, b.price, b.author, br.name as branch FROM book_sales bs
    RIGHT JOIN users u
        ON bs.user_id = u.id
    JOIN books b
        ON bs.book_id = b.id
    JOIN branches br
        ON bs.branch_id = br.id;
"""

def add_book_sales(cursor):
    pass