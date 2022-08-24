import os
import psycopg2

from dotenv import load_dotenv
load_dotenv()

def connect_db():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            host=os.getenv("DB_HOST"),
        )
        cursor = connection.cursor()

        # cursor.execute("DROP TABLE products")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users " +
            "(id SERIAL PRIMARY KEY, name TEXT, surname TEXT, email TEXT UNIQUE, phone TEXT UNIQUE, isAdmin BOOLEAN)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS admins (login TEXT UNIQUE, password TEXT)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS products (id SERIAL PRIMARY KEY, name TEXT UNIQUE, description TEXT, img TEXT)"
        )
        connection.commit()
        # cursor.close()
        # connection.close()
        return connection
    except Exception as error:
        print(f"Connection error: {error}")

