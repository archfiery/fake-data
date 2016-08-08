from .address import *
from .company import *
from .personal_data import *

'''
The amount of information we capture is small, but will be enlarged through iterations

Generate numP number of people, and 
numC number of companies

Each person is associated with a company, via different relationships
WORKS_AT / OWNS

Each company is associated with an address

There are 4 files generated

person.tsv
[name, gender, dob, email, mobile, phone]

company.tsv
[name, (start, end), isSixHourClosure]

address.tsv
[number, street, suburb, postcode, state, country]

person_company.tsv
[person_name, company_name, WORKS_AT / OWNS]

company_address.tsv
[company_name, address]

'''
def gen(numP, numC):
    person_file = open('person.tsv', 'wb+')
    person_list = list()
    for i in range(numP):
        d = dict()
        fng = first_name()
        fn, gender = fng[0], fng[1]
        ln = last_name()
        d['name'] = ' '.join([fn, ln]).strip()
        d['email'] = email(fn, ln)
        d['dob'] = dob()
        d['gender'] = gender
        d['mobile'] = mobile()
        d['phone'] = landline()
        p = Person(d)
        person_file.write((p.tsv() + '\n').encode())
    person_file.close()
   
    company_file = open('company.tsv', 'wb+')
    for i in range(numC):
        d = dict()
        d['name'] = company_name()
        d['openingHours'] = '6:00-23:00'
        d['isSixHourClosure'] = True
        c = Company(d)
        company_file.write((c.tsv() + '\n').encode())
    company_file.close()

