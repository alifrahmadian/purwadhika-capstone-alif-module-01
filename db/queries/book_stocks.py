def get_book_stocks():
    return """
        SELECT 
            bs.id, b.name as book_name, b.price, b.author,
            br.name as branch, bs.stock 
        FROM book_stocks bs
        JOIN books b
            ON bs.book_id = b.id
        JOIN branches br
            ON bs.branch_id = br.id;
    """

def get_book_stock_by_name_and_branch(book_name:str, branch_id:int):
    pass

def add_book_stock():
    pass

def update_book_stock_by_book_and_branch(book_id:int, branch_id:int):
    pass