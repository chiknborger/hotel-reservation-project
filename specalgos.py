import re

def get_name():
    #2-30 letters
    #special names like Mary Jane, Jean-Baptiste, O'Brien
    while True:
        name = input(">> ").strip()
        if len(name) < 2 or len(name) > 30:
            print("Name must be 2-30 characters!")
            continue
        if not name[0].isalpha() or not name[-1].isalpha():
            print("Name must start and end with a letter!")
            continue
        ok = True
        for i in range(len(name)):
            c = name[i]
            if c.isalpha():
                continue
            if c in " -'" and name[i - 1] not in " -'":
                continue
            ok = False
        if ok:
            return name
        print("Invalid name! Letters only (no numbers or repeated symbols).")


def get_email():
    #email domain
    while True:
        email = input(">> ").strip().lower()
        if len(email) > 254:
            print("Email is too long!")
            continue
        pattern = r"[a-z0-9]+([._%+-][a-z0-9]+)*@[a-z0-9]+(-[a-z0-9]+)*(\.[a-z0-9]+(-[a-z0-9]+)*)*\.[a-z]{2,10}"
        if re.fullmatch(pattern, email):
            return email
        print("Invalid email! Example: name@gmail.com")


def get_phone():
    #any country code
    #spaces dashesn not allowed
    while True:
        phone = input(">> ").strip()
        phone = phone.replace(" ", "").replace("-", "")
        digits = phone
        if phone.startswith("+"):
            digits = phone[1:]
        if not digits.isdigit():
            print("Invalid phone number! Digits only, with an optional + at the start.")
            continue
        if len(digits) < 8 or len(digits) > 15:
            print("Phone number must have 8-15 digits!")
            continue
        if digits == digits[0] * len(digits):
            print("Invalid phone number!")    
            continue
        return phone
