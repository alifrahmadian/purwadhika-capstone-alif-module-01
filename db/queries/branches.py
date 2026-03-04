def get_branches():
    return "SELECT * FROM branches"

def get_branch_by_name(cursor, name:str):
    query = """
        SELECT name FROM branches
        WHERE name = %s
        LIMIT 1;
"""
    cursor.execute(query, (name, ))
    return cursor.fetchone()

def get_branch_by_address(cursor, address:str):
    query = """
        SELECT address FROM branches
        WHERE address = %s
        LIMIT 1;
"""

    cursor.execute(query, (address, ))
    return cursor.fetchone()

def add_branch(cursor, name:str, address:str, city:str, province:str):
    query = """
        INSERT INTO branches (name, address, city, province)
        VALUES(%s, %s, %s, %s);
"""

    values = (name.title(), address.title(), city, province)
    cursor.execute(query, values)