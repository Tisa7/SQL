from connection import connect_db

def read_user():
    id = int(input("Enter id to read "))
    with connect_db() as conn:
        data = conn.execute(
            f'''
            SELECT * FROM users WHERE id = {id}
            '''
        ).fetchone()
    print("\nName: ",data[1])
    print("Age: ",data[2])
    print("Address:",data[3])

if __name__ == "__main__":
    read_user()