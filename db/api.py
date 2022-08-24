from db.index import connect_db

#Users
def insert_user(user):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (name, surname, email, phone) VALUES (%s, %s, %s, %s)",
        (user["name"], user["surname"], user["email"], user["phone"])
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
        "INSERT INTO products (name, description, img) VALUES (%s, %s, %s)",
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
    product = cursor.fetchall()
    return list(product[0])
