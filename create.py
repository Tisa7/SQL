from connection import connect_db

def create_user():
    name = input("Enter user name ")
    age = int(input("Enter age "))
    address = input("Enter address ")
    with connect_db() as conn:
        conn.execute(
            f'''
            INSERT INTO users (name,age,address) VALUES ('{name}',{age},'{address}')
            '''
        )
    print("User created Successfully !!!!")

if __name__ == "__main__":
    create_user()