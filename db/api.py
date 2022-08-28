from db.index import connect_db

#Users
def find_user(login):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
       f"SELECT json_agg(admins) FROM admins WHERE login = '{login}'"
    )
    res = cursor.fetchone()[0][0]
    return res

def insert_user(user):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (name, surname, email, phone, lang, userid) VALUES (%s, %s, %s, %s, %s, %s)",
        (user["name"], user["surname"], user["email"], user["phone"], user["lang"], user["userid"])
    )
    connection.commit()
    get_users()
    # connection.close()

def get_users():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    res = cursor.fetchall()

    print(res)

    # connection.close()

def check_if_user_exists(id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(f"SELECT EXISTS(SELECT 1 FROM users WHERE userid = {id})")
    res = cursor.fetchone()[0]

    return res

#Products
def get_products():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT json_agg(products) FROM products")
    products = cursor.fetchall()

    return [] if len(products) == 0 else list(products)[0][0]

def insert_product(product):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO products (name, description, image) VALUES (%s, %s, %s)",
        (product["name"], product["description"], product["image"])
    )

    connection.commit()

def delete_product(id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        f"DELETE FROM products WHERE id = {id}"
    )
    connection.commit()

def get_product(id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        f"SELECT json_agg(products) FROM products WHERE id = {id}"
    )
    product = cursor.fetchone()
    return product[0][0]

def edit_product(edited, id):
    connection = connect_db()
    cursor = connection.cursor()

    update_values = ""
    for index, values in enumerate(edited.items()):
        print(index, len(edited.items()))
        update_values += f"{values[0]} = '{values[1]}'{', ' if index + 1 != len(edited.items()) else ''}"

    cursor.execute(
        f"UPDATE products SET {update_values} WHERE id = {id}"
    )
    connection.commit()
