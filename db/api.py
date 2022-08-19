import psycopg2
from db.index import connect_db

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

