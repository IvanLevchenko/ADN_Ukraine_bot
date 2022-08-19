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

        # cursor.execute("DROP TABLE users")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users " +
            "(id SERIAL PRIMARY KEY, name TEXT, surname TEXT, email TEXT UNIQUE, phone TEXT UNIQUE)"
        )

        # cursor.close()
        # connection.close()
        return connection
    except Exception as error:
        print(f"Connection error: {error}")

