class Person():
    pass


someone = Person()


class Person():
    def __init__(self):
        pass


class Person():
    def __init__(self, name):
        self.name = name


hunter = Person('Elmer Fudd')

print('The mighty hunter: ', hunter.name)


class Car():
    pass


class Yugo(Car):
    pass


give_me_a_car = Car()
give_me_a_yugo = Yugo()


class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    pass


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()

give_me_a_yugo.exclaim()


class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")


give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()

give_me_a_yugo.exclaim()


class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)

print(doctor.name)

print(lawyer.name)


class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()

give_me_a_car.need_a_push()


class Person():
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

bob.name

bob.email


class EmailPerson(Person):
    def __init__(self, name, email):
        self.name = name
        self.email = email


car = Car()
car.exclaim()

Car.exclaim(car)


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)


fowl = Duck('Howard')
fowl.name

fowl.get_name()

fowl.name = 'Daffy'

fowl.name

fowl.set_name('Daffy')

fowl.name


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


fowl = Duck('Howard')
fowl.name

fowl.name = 'Donald'

fowl.name


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
c.radius

c.diameter

c.radius = 7
c.diameter

c.diameter = 20


class Duck():
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


fowl = Duck('Howard')
fowl.name

fowl.name = 'Donald'

fowl.name

fowl.__name

fowl._Duck__name


class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()


class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')


CoyoteWeapon.commercial()


class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())


class BabblingBrook():
    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'


brook = BabblingBrook()


def who_says(obj):
    print(obj.who(), 'says', obj.says())


who_says(hunter)

who_says(hunted1)

who_says(hunted2)

who_says(brook)


class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')

first.equals(second)

first.equals(third)


class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')
first == second

first == third

first = Word('ha')
first

print(first)


class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("'  self.text  '")'


first = Word('ha')
first          # uses __repr__

print(first)   # uses __str__


class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description,
            'bill and a', self.tail.length, 'tail')


a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
duck

duck.bill

duck.tail

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
duck2

duck2 = Duck(bill = 'wide orange', tail = 'long')

duck3 = duck2._replace(tail='magnificent', bill='crushing')
duck3

duck_dict = {'bill': 'wide orange', 'tail': 'long'}
duck_dict

duck_dict['color'] = 'green'
duck_dict

duck.color = 'green'

