from connection import connect_db

def create_table():
    with connect_db() as conn:
        conn.execute(
            '''
            CREATE TABLE users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            address TEXT
            )
            '''
        )
        
if __name__ == "__main__":
    create_table()
