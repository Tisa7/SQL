from connection import connect_db

def update_user():
    id = int(input("Enter id to update "))
    column = input("Enter column that you want to update (name,age,address) ")
    new_value = input(f"Enter new value for column {column} ")
    with connect_db() as conn:
        conn.execute(
            f'''
            UPDATE users SET {column} = '{new_value}' WHERE id = {id}
            '''
        )

    print("User updated successfully!!!")


if __name__ == "__main__":
    update_user()