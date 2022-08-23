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
    connection.close()

def get_users():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    res = cursor.fetchall()

    print(res)

    connection.close()

#Products
def get_products():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT json_agg(products) FROM products")
    products = cursor.fetchall()

    return list(products)[0][0]

def insert_product(product):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO products VALUES('%s', '%s', '%s')" % (product["name"], product["description"], product["image"])
    )

    connection.commit()
