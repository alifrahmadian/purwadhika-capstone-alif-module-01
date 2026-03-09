def get_users():
    return "SELECT * from USERS"

def get_user_by_id(cursor, id:int):
    query = """
        SELECT * FROM users
        WHERE id = %s
"""

    cursor.execute(query, (id, ))
    return cursor.fetchone()

def get_user_by_email(cursor, email:str):
    query = """
        SELECT * FROM users
        WHERE email = %s;
"""

    cursor.execute(query, (email, ))
    return cursor.fetchone()


def get_user_by_phone_number(cursor, phone_number:str):
    query = """
        SELECT * FROM users
        WHERE phone_number = %s;
"""

    cursor.execute(query, (phone_number, ))
    return cursor.fetchone()

def add_user(cursor, name:str, email:str, phone_number:str):
    query = """
        INSERT INTO users (name, email, phone_number)
        VALUES(%s, %s, %s);
"""

    values = (name.title(), email, phone_number)
    cursor.execute(query, values)

def update_user_points(cursor, user_id:int, points:int):
    query = """
        UPDATE users
        SET points = %s
        WHERE id = %s;
"""

    values = (points, user_id)
    cursor.execute(query, values)