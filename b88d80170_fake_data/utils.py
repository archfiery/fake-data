import random

def pickone(L):
    return L[random.randint(0, len(L) - 1)]

# c is a float number between 0 and 1
def pickchance(c):
    return random.random() <= c

def randomIntList(numdigit):
    l = str()
    for i in range(numdigit):
        l += str(random.randint(0, 9))
    return l
