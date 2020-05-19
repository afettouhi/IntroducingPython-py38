# 60 sec/min * 60 min/hr * 24 hr/day
seconds_per_day = 86400

seconds_per_day = 86400 # 60 sec/min * 60 min/hr * 24 hr/day

# I can say anything here, even if Python doesn't like it,
# because I'm protected by the awesome
# octothorpe.

print("No comment: quotes make the # harmless.")

alphabet = ''
alphabet += 'abcdefg'
alphabet += 'hijklmnop'
alphabet += 'qrstuv'
alphabet += 'wxyz'

alphabet = 'abcdefg' + \
     'hijklmnop' + \
     'qrstuv' + \
     'wxyz'

1 + 2 +

1 + 2 + \
3

disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

furry = True
small = True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's a human. Or a hairless bear.")

x = 7

x == 5

x == 7

5 < x

x < 10

5 < x and x < 10

(5 < x) and (x < 10)

5 < x or x < 10

5 < x and x > 10

5 < x and not x > 10

5 < x < 10

5 < x < 10 < 999

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")

letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' \
    or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')

vowels = 'aeiou'
letter = 'o'
letter in vowels

if letter in vowels:
    print(letter, 'is a vowel')

vowel_set = {'a', 'e', 'i', 'o', 'u'}
letter in vowel_set

vowel_list = ['a', 'e', 'i', 'o', 'u']
letter in vowel_list

vowel_tuple = ('a', 'e', 'i', 'o', 'u')
letter in vowel_tuple

vowel_dict = {'a': 'apple', 'e': 'elephant',
              'i': 'impala', 'o': 'ocelot', 'u': 'unicorn'}
letter in vowel_dict

count = 1
while count <= 5:
    print(count)
    count += 1

while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())

while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':      # quit
        break
    number = int(value)
    if number % 2 == 0:   # an even number
       continue
    print(number, "squared is", number*number)

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:  # break not called
    print('No even number found')

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

for rabbit in rabbits:
    print(rabbit)

word = 'cat'
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
                  'person': 'Col. Mustard'}
for card in accusation:  #  or, for card in accusation.keys():
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:  # no break means no cheese
    print('This is not much of a cheese shop, is it?')

cheeses = []
found_one = False
for cheese in cheeses:
    found_one = True
    print('This shop has some lovely', cheese)
    break

if not found_one:
    print('This is not much of a cheese shop, is it?')

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

list( zip(english, french) )

dict( zip(english, french) )

for x in range(0,3):
    print(x)

list( range(0, 3) )

for x in range(2, -1, -1):
    print(x)

list( range(2, -1, -1) )

list( range(0, 11, 2) )

number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
number_list

number_list = []
for number in range(1, 6):
    number_list.append(number)

number_list

number_list = list(range(1, 6))
number_list

number_list = [number for number in range(1,6)]
number_list

number_list = [number-1 for number in range(1,6)]
number_list

a_list = [number for number in range(1,6) if number % 2 == 1]
a_list

a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)

a_list

rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row, col)

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

for row, col in cells:
    print(row, col)

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
letter_counts

a_set = {number for number in range(1,6) if number % 3 == 1}
a_set

number_thing = (number for number in range(1, 6))

type(number_thing)

for number in number_thing:
    print(number)

number_list = list(number_thing)
number_list

try_again = list(number_thing)
try_again

def do_nothing():
    pass

do_nothing()

def make_a_sound():
    print('quack')

make_a_sound()

def agree():
   return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')

def echo(anything):
   return anything + ' ' + anything

echo('Rumplestiltskin')

def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color "  + color +  "."

comment = commentary('blue')

print(comment)

print(do_nothing())

thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

if thing is None:
    print("It's nothing")
else:
    print("It's something")

def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")

is_none(None)

is_none(True)

is_none(False)

is_none(0)

is_none(0.0)

is_none(())

is_none([])

is_none({})

is_none(set())

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chicken', 'cake')

menu('beef', 'bagel', 'bordeaux')

menu(entree='beef', dessert='bagel', wine='bordeaux')

menu('frontenac', dessert='flan', entree='fish')

def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chicken')

menu('dunkelfelder', 'duck', 'doughnut')

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')

buggy('b')   # expect ['b']

def works(arg):
    result = []
    result.append(arg)
    return result

works('a')

works('b')

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy('a')

nonbuggy('b')

def print_args(*args):
    print('Positional argument tuple:', args)

print_args()

print_args(3, 2, 1, 'wait!', 'uh...')

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

def echo(anything):
    'echo returns its input argument'
    return anything

def print_if_true(thing, check):
    """
    Prints the first argument if a second argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    """
    if check:
        print(thing)

help(echo)

print(echo.__doc__)

def answer():
    print(42)

answer()

def run_something(func):
    func()

run_something(answer)

type(run_something)

def add_args(arg1, arg2):
    print(arg1 + arg2)

type(add_args)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)

def sum_args(*args):
   return sum(args)

def run_with_positional_args(func, *args):
   return func(*args)

run_with_positional_args(sum_args, 1, 2, 3, 4)

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

outer(4, 7)

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

knights('Ni!')

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

type(a)

type(b)

a

b

a()

b()

def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):   # give that prose more punch
    return word.capitalize() + '!'

edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalize() + '!')

sum(range(1, 101))

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

my_range

ranger = my_range(1, 5)
ranger

for x in ranger:
    print(x)

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
   return a + b

add_ints(3, 5)

cooler_add_ints = document_it(add_ints)  # manual decorator assignment
cooler_add_ints(3, 5)

@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

@square_it
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)

print_global()

def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

change_and_print_global()

def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local()

animal

id(animal)

animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

animal

change_and_print_global()

animal

animal = 'fruitbat'
def change_local():
    animal = 'wombat'  # local variable
    print('locals:', locals())

animal

change_local()

print('globals:', globals()) # reformatted a little for presentation

animal

def amazing():
    """This is the amazing function.
    Want to see it again?"""
    print('This function is named:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)

amazing()

short_list = [1, 2, 3]
position = 5
short_list[position]

short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, ' but got',
           position)

short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)

class UppercaseException(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)

try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)