from cli import start, login, admin_menu, client_menu, sys_clear, sys_pause
from dbops import add_user, is_admin

start()
print("Hotel Reservation System")

while True:
    print("-----Main Menu-----")
    print("[1] Login")
    print("[2] Register")
    print("[3] Quit")

    choice = input(">> ")
    user = None
    if choice == "1":
        user = login()
    elif choice == "2":
        user = add_user()
    elif choice == "3":
        break
    else:
        print("Invalid option!")

    if user is not None:
        sys_pause()
        if is_admin(user):
            admin_menu(user)
        else:
            client_menu(user)
    else:
        sys_pause()
    sys_clear()
