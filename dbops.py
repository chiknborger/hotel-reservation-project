import csv
import os

from globalvariables import *
from algos import get_int, get_float, yes_no, choose_item
from specalgos import get_name, get_email, get_phone
from password import get_password
from classes import input_date, text_to_date, total_cost

#read and write 
def read_rows(file):
    rows = []
    if not os.path.exists(file):
        return rows
    with open(file, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                rows.append(row)
    return rows


def write_rows(file, rows):
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def add_row(file, row):
    with open(file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)


#users

def find_email(email):
    for user in read_rows(USERS_FILE):
        if user[2] == email:
            return user
    return None


def find_phone(phone):
    for user in read_rows(USERS_FILE):
        if user[3] == phone:
            return user
    return None


def is_admin(user):
    #first user created is admin
    rows = read_rows(USERS_FILE)
    return rows[0][2] == user[2]


def add_user():
    print("-----Account Creation-----")
    print("First Name")
    first_name = get_name()
    print("Last Name")
    last_name = get_name()

    print("Email Address")
    while True:
        email = get_email()
        if find_email(email) is not None:
            print("Email Address taken!")
        else:
            break

    print("Phone Number")
    while True:
        phone = get_phone()
        if find_phone(phone) is not None:
            print("Phone number taken!")
        else:
            break

    print("Password")
    password = get_password()

    user = [first_name, last_name, email, phone, password]
    add_row(USERS_FILE, user)
    print("User created successfully.")
    return user


def find_room(number):
    for room in read_rows(ROOMS_FILE):
        if room[0] == str(number):
            return room
    return None


def price_of(room):
    return float(room[2])


def save_room(room, is_new):

    rows = read_rows(ROOMS_FILE)
    if is_new:
        rows.append(room)
    else:
        for i in range(len(rows)):
            if rows[i][0] == room[0]:
                rows[i] = room
    rows.sort(key=price_of)
    write_rows(ROOMS_FILE, rows)


def show_room(room):
    print("")
    print("Room Number: " + room[0])
    print("Type: " + room[1])
    print("Price: " + room[2] + "kr per night")


def show_all_rooms():
    rooms = read_rows(ROOMS_FILE)
    if len(rooms) == 0:
        print("There are no rooms!")
        return
    for room in rooms:
        show_room(room)


def ask_price():
    print("Price per night")
    while True:
        price = get_float()
        if price > 0:
            return price
        print("Price must be more than 0!")


def add_room():
    print("Room Number")
    while True:
        number = get_int()
        if number <= 0:
            print("Invalid room number!")
        elif find_room(number) is not None:
            print("Room taken!")
        else:
            break

    print("Type")
    room_type = choose_item(ROOM_TYPES)
    price = ask_price()

    save_room([str(number), room_type, str(price)], True)
    print("Room added successfully.")


def edit_room():
    if len(read_rows(ROOMS_FILE)) == 0:
        print("There are no rooms!")
        return
    show_all_rooms()
    print("")
    print("Room Number")
    number = get_int()
    room = find_room(number)
    if room is None:
        print("Room not found!")
        return
    print("Type")
    room[1] = choose_item(ROOM_TYPES)
    room[2] = str(ask_price())
    save_room(room, False)
    print("Room info edited successfully.")


def delete_room():
    if len(read_rows(ROOMS_FILE)) == 0:
        print("There are no rooms!")
        return
    show_all_rooms()
    print("")
    print("Room Number")
    number = get_int()
    if find_room(number) is None:
        print("Room not found!")
        return
    rooms = []
    for room in read_rows(ROOMS_FILE):
        if room[0] != str(number):
            rooms.append(room)
    write_rows(ROOMS_FILE, rooms)
    reservations = []
    for res in read_rows(RESERVATIONS_FILE):
        if res[0] != str(number):
            reservations.append(res)
    write_rows(RESERVATIONS_FILE, reservations)
    print("Room deleted successfully.")


#reservations

def room_is_free(room_number, start, end):
    for res in read_rows(RESERVATIONS_FILE):
        if res[0] != room_number:
            continue
        res_start = text_to_date(res[2])
        res_end = text_to_date(res[3])
        if start < res_end and end > res_start:
            return False
    return True


def ask_dates():
    print("Enter the dates you want a room for.")
    print("Check-in date")
    start = input_date()
    print("Check-out date")
    end = input_date()
    if start == end:
        print("The two dates can't be the same!")
        return None
    if end < start:
        start, end = end, start
    return start, end


def get_available_rooms(start, end):
    available = []
    for room in read_rows(ROOMS_FILE):
        if room_is_free(room[0], start, end):
            available.append(room)
    return available


def see_available_rooms():
    if len(read_rows(ROOMS_FILE)) == 0:
        print("There are no rooms yet!")
        return
    dates = ask_dates()
    if dates is None:
        return
    available = get_available_rooms(dates[0], dates[1])
    if len(available) == 0:
        print("No rooms available on these dates.")
        return
    for room in available:
        show_room(room)


def book_room(user):
    if len(read_rows(ROOMS_FILE)) == 0:
        print("There are no rooms yet!")
        return
    dates = ask_dates()
    if dates is None:
        return
    start = dates[0]
    end = dates[1]

    available = get_available_rooms(start, end)
    if len(available) == 0:
        print("No rooms available on these dates.")
        return
    for room in available:
        show_room(room)

    print("")
    print("Do you wish to continue?")
    if not yes_no():
        return

    print("Room Number")
    while True:
        number = get_int()
        chosen = None
        for room in available:
            if room[0] == str(number):
                chosen = room
        if chosen is None:
            print("Room unavailable! Pick one from the list.")
        else:
            break

    add_row(RESERVATIONS_FILE, [chosen[0], user[2], start.isoformat(), end.isoformat()])
    cost = total_cost(float(chosen[2]), start, end)
    print("Room booked successfully.")
    print("Total with tax: " + str(round(cost, 2)) + "kr")
