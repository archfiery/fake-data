'''
https://en.wikipedia.org/wiki/Telephone_numbers_in_Australia
'''

import random
from utils import *

def randomIntList():
    l = str()
    for i in range(8):
        l += str(random.randint(0, 9))
    return l 

def landline():
    prefix = ['02', '03', '07', '08']
    return pickone(prefix) + randomIntList()

def mobile():
    prefix = ['04', '05']
    return  pickone(prefix) + randomIntList()
