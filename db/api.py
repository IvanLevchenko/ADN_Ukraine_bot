import psycopg2

def register_user(connection, user):
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users (name, surname, email, phone) VALUES (%s, %s, %s, %s)",
        (user.name, user.surname, user.email, user.phone)
    )

    connection.close()