'''
https://en.wikipedia.org/wiki/Telephone_numbers_in_Australia
'''

from .utils import *

def landline():
    prefix = ['02', '03', '07', '08']
    return pickone(prefix) + randomIntList(8)

def mobile():
    prefix = ['04', '05']
    return  pickone(prefix) + randomIntList(8)
