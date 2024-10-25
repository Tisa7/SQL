from create import create_user
from read import read_user
from delete import delete_user
from update import update_user

while True:
    choice = input("\nEnter your choice...c/r/u/d/ ").lower()
    match choice:
        case 'c':
            create_user()
        case 'r':
            read_user()
        case 'u':
            update_user()
        case 'd':
            delete_user()
        case _:
            print("Invalid choice...")

    repeat = input("\nDo you wish to continue... y/n? ").lower()
    if repeat != 'y':
        print("\nThank you, Have a nice day.")
        break
