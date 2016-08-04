from .utils import *

def street():
    names = ['Bridge', 'Church', 'Sloane', 'Lincoln', 'Harris', 'Meadow', 'Beech', 'Essex', 'Sussex', 'Madison',\
             'Broad', 'Cedar', 'Maple', 'River', 'Washington', 'Pitt', 'Oak', 'Hillside', 'Miller', 'Jefferson',\
             'Monroe', 'New', 'Victoria', 'Franklin', 'Highland', 'Market', 'Geroge', 'Wellington', 'Vine', 'Walnut',\
             'Park', 'Green', 'Cherry', 'Chestnut', 'Mango']
    types = ['Avenue', 'Road', 'Street', 'Drive', 'Way']
    suffix = ['North', 'South', 'East', 'West']
    
    n = pickone(names)
    t = pickone(types)
    full_street_name = n + ' ' + t

    if pickchance(0.2):
        return full_street_name + ' ' + pickone(suffix)

    return full_street_name

def state():
    names = ['ACT', 'NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA']
    return pickone(names)

def format_address(L):
    return (' '.join(L)).strip()

def address():
    return format_address(['No.', str(random.randint(1, 1999)), street(), state()])
