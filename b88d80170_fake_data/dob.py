import calendar
import random

feb = 2
month30 = set([4, 6, 9, 11])
month31 = set([1, 3, 5, 7, 8, 10, 12])

def validDOB(L):
    year, month, day = L[0], L[1], L[2]
    if (month in month30):
        if day > 30:
            return False
    if (month == feb):
        if year % 4 == 0 and day > 29:
            return False
        if year % 4 != 0 and day > 28:
            return False

    return True

def dobRandom():
    year = random.randint(1950, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 31)

    return [year, month, day]

def dobFormat(L):
    return '-'.join([str(n) if n >= 10 else '0' + str(n) for n in L])

def dob():
    while (True):
        L = dobRandom()
        if (validDOB(L)):
            return dobFormat(L)

