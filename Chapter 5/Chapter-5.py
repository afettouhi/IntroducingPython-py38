print("This interactive snippet works.")

print("This standalone program works!")


def get_description():
    import random
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return random.choice(possibilities)


import random


def get_description():
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return random.choice(possibilities)


get_description()

import report as wr

description = wr.get_description()
print("Today's weather:", description)

from report import get_description

description = get_description()
print("Today's weather:", description)

from report import get_description as do_it

description = do_it()
print("Today's weather:", description)

import sys

for place in sys.path:
    print(place)

periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
carbon

periodic_table

helium = periodic_table.setdefault('Helium', 947)
helium

periodic_table

from collections import defaultdict

periodic_table = defaultdict(int)

periodic_table['Hydrogen'] = 1
periodic_table['Lead']

periodic_table

from collections import defaultdict


def no_idea():
    return 'Huh?'


bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
bestiary['A']

bestiary['B']

bestiary['C']

bestiary = defaultdict(lambda: 'Huh?')
bestiary['E']

from collections import defaultdict

food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1
for food, count in dict_counter.items():
    print(food, count)

from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
breakfast_counter

breakfast_counter.most_common()

breakfast_counter.most_common(1)

breakfast_counter
Counter({'spam': 3, 'eggs': 1})

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
lunch_counter

breakfast_counter + lunch_counter

breakfast_counter - lunch_counter

lunch_counter - breakfast_counter

breakfast_counter & lunch_counter

breakfast_counter | lunch_counter

quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk nyuk!',
}
for stooge in quotes:
    print(stooge)

from collections import OrderedDict

quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])

for stooge in quotes:
    print(stooge)


def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


palindrome('a')

palindrome('racecar')

palindrome('')

palindrome('radar')

palindrome('halibut')


def another_palindrome(word):
    return word == word[::-1]


another_palindrome('radar')

another_palindrome('halibut')

import itertools

for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

import itertools

for item in itertools.cycle([1, 2]):
    print(item)

import itertools

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

import itertools


def multiply(a, b):
    return a * b


for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)

from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])

print(quotes)

pprint(quotes)
