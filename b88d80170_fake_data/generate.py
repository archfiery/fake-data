from .address import *
from .company import *
from .personal_data import *
from .name import first_name

"""
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

"""


def gen(num_person, num_company):
    person_file = open('person.tsv', 'wb+')
    person_set = set()
    for i in range(num_person):
        d = dict()
        fng = first_name()
        fn, gender = fng[0], fng[1]
        ln = last_name()
        d['id'] = i
        d['name'] = ' '.join([fn, ln]).strip()
        d['email'] = email(fn, ln)
        d['dob'] = dob()
        d['gender'] = gender
        d['mobile'] = mobile()
        d['phone'] = landline()
        p = Person(d)
        person_set.add(p)
        person_file.write((p.tsv() + '\n').encode())
    person_file.close()

    company_file = open('company.tsv', 'wb+')
    company_set = set()
    for i in range(num_company):
        d = dict()
        d['name'] = company_name()
        d['openingHours'] = '6:00-23:00'
        d['isSixHourClosure'] = True
        c = Company(d)
        company_set.add(c)
        company_file.write((c.tsv() + '\n').encode())
    company_file.close()


