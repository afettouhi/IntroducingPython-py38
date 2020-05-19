# 4.1
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

# 4.2
guess_me = 7
start = 1
while start <= guess_me:
    print('too low')
    if start == guess_me:
        print('found it!')
    if start > guess_me:
        print('oops')
    start += 1

# 4.3
my_list = [3, 2, 1, 0]

for x in my_list:
    print(x)

# 4.4
number_list = []
for number in range(10):
    number_list.append(number)

# 4.5
my_square = 'squares'
squares = {x: my_square for x in range(10)}

# 4.6
odd = {number for number in range(10) if number % 2 == 1}

# 4.7
generator = (('Got ', x) for x in range(10))
for i in generator:
    print(i)


# 4.8
def good():
    return ['Harry', 'Ron', 'Hermione']


good()


# 4.9
def get_odds():
    a = (x for x in range(10) if x % 2 != 0)
    c = []
    for i in a:
        c.append(i)
    print(c[2])


get_odds()


# 4.10
def test(func):
    def new_function(*args, **kwargs):
        print('start')
        answer = 'end'
        return answer

    return new_function


@test
def func():
    pass


func()


# 4.11
class OopsException(Exception):
    pass


words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        # raise UppercaseException(word)
        try:
            raise OopsException('Caught an oops')
        except OopsException as exc:
            print(exc)

# 4.12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = {v: k for v, k in zip(titles, plots)}
print(movies)
