from .address import address
from .company import company_name
from .dob import dob
from .email import email
from .name import name_format, first_name, last_name, name
from .phone import mobile, landline
from .tsv import TSV

class Person(TSV):
    def __init__(self, argv):
        if 'name' in argv:
            self.name = argv['name']
        if 'gender' in argv:
            self.gender = argv['gender']
        #if 'company' in argv:
        #    self.company = argv['company']
        if 'dob' in argv:
            self.dob = argv['dob']
        #if 'address' in argv:
        #    self.address = argv['address']
        if 'email' in argv:
            self.email = argv['email']
        if 'mobile' in argv:
            self.mobile = argv['mobile']
        if 'phone' in argv:
            self.phone = argv['phone']

    def to_list(self):
        return [str(i) for i in [self.name, self.gender, self.dob, self.email, self.mobile, self.phone]]

    def __str__(self):
        return '\n'.join(self.to_list())

    def name(self):
        return name
        
    def tsv(self):
        return '\t'.join(self.to_list())

def person_without_name():
    args = dict()
    args['dob'] = dob()
    args['address'] = address()
    args['mobile'] = mobile()
    args['phone'] = landline()

    return args

def male_person():
    args = person_without_name()
    fn, ln = male_first_name(), last_name()
    args['name'] = name_format(fn, ln)
    args['email'] = email(fn, ln)
    args['gender'] = 'M'

    return Person(args)

def female_person():
    args = person_without_name()
    fn, ln = female_first_name(), last_name()
    args['name'] = name_format(fn, ln)
    args['email'] = email(fn, ln)
    args['gender'] = 'F'

    return Person(args)
