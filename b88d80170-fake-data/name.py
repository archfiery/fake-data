from utils import *

# It has English, Chinese, Japanese and Korean surnames
last_name_pool = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson',\
                  'Moore', 'Taylor', 'Jackson', 'Nelson', 'Young', 'Hall', 'Allen', 'Price', 'Rogers',\
                  'Martin', 'Harris', 'Thompson', 'Green', 'Scott', 'Hill', 'Lopez', 'King', 'Perry',\
                  'Lee', 'Walker', 'Wright', 'White', 'Clark', 'Collins', 'Cox', 'Diaz', 'Murphy',\
                  'Simmons', 'Parker', 'Wayne', 'Phillips', 'Turner', 'Wang', 'Li', 'Zhang', 'Ong',\
                  'Ng', 'Wu', 'Wong', 'Zhu', 'Zhou', 'Song', 'Chen', 'Chan', 'Dan', 'Chino', 'Hara',\
                  'Hiraga', 'Daishi', 'Takeshi', 'Kim', 'Park', 'Kong', 'Ka', 'Seo']

# It only has English first names
female_first_name_pool = ['Emily', 'Chloe', 'Megan', 'Emma', 'Lauren', 'Amy', 'Lucy', 'Olivia', 'Katie', 'Jessica',\
                          'Sarah', 'Beth', 'Jade', 'Anna', 'Zoe', 'Lydia', 'Erin', 'Rosie', 'Molly', 'Grace', 'Lisa']

male_first_name_pool = ['James', 'Harry', 'Jack', 'Alex', 'Ben', 'Daniel', 'Tom', 'Adam', 'Ryan', 'Sam', 'Matthew',\
                        'Joe', 'Anthony', 'Nick', 'Jamie', 'Henry', 'Robert', 'Mark', 'Joseph', 'George', 'Lewis']


def name_format(fn, ln):
    return ' '.join([fn, ln]).strip()

def female_first_name():
    return pickone(female_first_name_pool)

def male_first_name():
    return pickone(male_first_name_pool)

def last_name():
    return pickone(last_name_pool)

def female_name():
    fn = female_first_name()
    ln = last_name()
    return name_format(fn, ln)

def male_name():
    fn = male_first_name()
    ln = last_name()
    return name_format(fn, ln)

def name():
    return pickone([male_name(), female_name()])
