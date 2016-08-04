from address import *
from company import *
from dob import *
from email import *
from name import *
from phone import *

class Person:
    def __init__(self, argv):
        if 'name' in argv:
            self.name = argv['name']
        if 'company' in argv:
            self.company = argv['company']
        if 'dob' in argv:
            self.dob = argv['dob']
        if 'address' in argv:
            self.address = argv['address']
        if 'email' in argv:
            self.email = argv['email']
        if 'phone' in argv:
            self.phone = argv['phone']
    def __str__(self):
        return self.name + '\n' + self.dob + '\n'\
        + self.address + '\n' + self.email + '\n' + self.phone

def male_person():
    args = dict()
    fn, ln = male_first_name(), last_name()
    args['name'] = name_format(fn, ln)
    args['dob'] = dob()
    args['address'] = address()
    args['email'] = email(fn, ln)
    args['phone'] = mobile()
    p = Person(args)

    print(p)

