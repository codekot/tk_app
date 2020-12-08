import sqlite3

DATABASE = "books.db"
TABLE = "book"

class Database:
    def __init__(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, 
            title text, author text, year integer, isbn integer)
            """)
        connection.commit()
        connection.close()

    def insert(self, title, author, year, isbn):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",
                       (title, author, year, isbn))
        connection.commit()
        connection.close()

    def view(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM book")
        rows = cursor.fetchall()
        connection.close()
        return rows

    def search(self, title=None, author=None, year=None, isbn=None):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
            (title, author, year, isbn))
        rows = cursor.fetchall()
        connection.close()
        return rows

    def delete(self, id):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM book WHERE id=?", (id,))
        connection.commit()
        connection.close()

    def update(self, id, title, author, year, isbn):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
            (title,author, year, isbn, id))
        connection.commit()
        connection.close()


#connect()
#insert("The Oil", "Smith Red", 2020, 1321214)
#print(view())
#print(search(year=1999))
#delete(1)
#update(2, title="The Eaff", author="John Smooth", year=2000, isbn=12312345)
#print(view())
