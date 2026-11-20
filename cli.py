#menus and screens
import os
import getpass
from dbops import *

def sys_clear():
    os.system("cls" if os.name == "nt" else "clear")

def sys_pause():
    input("\nPress Enter to continue...")

def login():
    print("------Login------")
    print("Email Address")
    email = get_email()
    user = find_email(email)
    if user is None:
        print("No account associated with this email was found")
        return None
    print("Password")
    password = getpass.getpass(">> ")
    if user[4] == password:
        print("Login successful!")
        return user
    print("Login failed!")
    return None


def client_menu(user):
    while True:
        sys_clear()
        print("-----Client Menu-----")
        print("Logged in as " + user[0] + " " + user[1])
        print("[1] See available rooms")
        print("[2] Book a room")
        print("[3] Logout")

        choice = input(">> ")
        if choice == "1":
            see_available_rooms()
        elif choice == "2":
            book_room(user)
        elif choice == "3":
            return
        else:
            print("Invalid option")
        sys_pause()


def admin_menu(user):
    while True:
        sys_clear()
        print("-----Admin Menu-----")
        print("Logged in as " + user[0] + " " + user[1])
        print("[1] Add room")
        print("[2] Edit room")
        print("[3] Delete room")
        print("[4] Show all rooms")
        print("[5] Logout")

        choice = input(">> ")
        if choice == "1":
            add_room()
        elif choice == "2":
            edit_room()
        elif choice == "3":
            delete_room()
        elif choice == "4":
            show_all_rooms()
        elif choice == "5":
            return
        else:
            print("Invalid option")
        sys_pause()


def first_setup():
    print("No data found; entering first-time setup...")
    print("Create the admin user:")
    add_user()
    sys_pause()


def start():
    sys_clear()
    if len(read_rows(USERS_FILE)) == 0:
        first_setup()
