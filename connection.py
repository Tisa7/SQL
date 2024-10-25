import sqlite3

def connect_db():
    return sqlite3.Connection("python_class.db")

if __name__ == "__main__":
    connect_db()