import sqlite3

DATABASE = "books.db"


def connect():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXITS book (id INTEGER PRIMARY KEY, 
        title text, author text, year integer, isbn integer)
        """)
    connection.commit()
    connection.close()

connect()
