from datetime import date
from algos import get_int
from globalvariables import TAX


def input_date():
    while True:
        print("Year")
        year = get_int()
        print("Month")
        month = get_int()
        print("Day")
        day = get_int()
        try:
            d = date(year, month, day)
        except ValueError:
            print("Invalid date!")
            continue
        if d < date.today():
            print("The date can't be in the past!")
            continue
        return d


def text_to_date(text):
    return date.fromisoformat(text)


def total_cost(price, start, end):
    nights = (end - start).days
    total = nights * price
    return total + total * TAX
