import random

feb = 2
month30 = {4, 6, 9, 11}
month31 = {1, 3, 5, 7, 8, 10, 12}


def valid_dob(l):
    year, month, day = l[0], l[1], l[2]
    if month in month30:
        if day > 30:
            return False
    if month == feb:
        if year % 4 == 0 and day > 29:
            return False
        if year % 4 != 0 and day > 28:
            return False

    return True


def dob_random():
    year = random.randint(1950, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 31)

    return [year, month, day]


def dob_format(l):
    return '-'.join([str(n) if n >= 10 else '0' + str(n) for n in l])


def dob():
    while True:
        l = dob_random()
        if valid_dob(l):
            return dob_format(l)
