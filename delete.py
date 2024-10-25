from connection import connect_db

def delete_user():
    id = int(input("Enter id to delete "))
    with connect_db() as conn:
        conn.execute(
            f'''
            DELETE FROM users WHERE id = {id}
            '''
        )

    print("User deleted successfully!!!")


if __name__ == "__main__":
    delete_user()