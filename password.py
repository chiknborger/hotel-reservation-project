import getpass

def get_password():
    while True:
        password = getpass.getpass(">> ")
        if len(password) < 8 or len(password) > 32:
            print("Password must be 8-32 characters!")
            continue
        if " " in password:
            print("Password can't contain spaces!")
            continue
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        for c in password:
            if c.islower():
                has_lower = True
            elif c.isupper():
                has_upper = True
            elif c.isdigit():
                has_digit = True
            else:
                has_special = True
        if has_lower and has_upper and has_digit and has_special:
            return password
        print("Password requires a lowercase letter, an uppercase letter, a number and a special character!")
