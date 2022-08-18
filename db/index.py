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
        connection.close()
    except Exception as error:
        print(f"Connection error: {error}")

