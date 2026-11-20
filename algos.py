def get_int():
    #whole number
    while True:
        try:
            return int(input(">> "))
        except ValueError:
            print("Invalid input!")


def get_float():
    #decimals for price
    while True:
        try:
            return float(input(">> "))
        except ValueError:
            print("Invalid input!")


def yes_no():
    while True:
        answer = input("[y/n] >> ").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        print("Invalid option!")


def choose_item(items):
    for i in range(len(items)):
        print("[" + str(i + 1) + "] " + items[i])
    while True:
        number = get_int()
        if 1 <= number <= len(items):
            return items[number - 1]
        print("Invalid option!")
