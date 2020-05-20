# 6.1
class Thing:
    pass


print(Thing)


class example(Thing):
    pass


print(example)


# 6.2
class Thing2:
    letters = 'abc'


Thing2.letters


# 6.3
class Thing3:
    def __init__(self, word):
        self.word = word

    def letters(self):
        print(self.word)


Thing3('xyz').letters()


# 6.4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


a = Element('Hydrogen', 'H', 1)

a.name

# 6.5
a = {'name': 'hydrogen', 'symbol': 'H', 'number': 1}
# hydrogen = Element(a['name'], a['symbol'],a['number'])
hydrogen = Element(**a)


# 6.6
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print('name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number))


hydrogen = Element(**a)
hydrogen.dump()


# 6.7
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return 'name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number)


hydrogen = Element(**a)

print(hydrogen)


# 6.8
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


hydrogen = Element(**a)

hydrogen.name


# 6.9
class Bear:
    def eat():
        return 'berries'


class Rabbit:
    def eat():
        return 'clover'


class Octothorpe:
    def eat():
        return 'campers'


print(Bear.eat())

print(Rabbit.eat())

print(Octothorpe.eat())


# 6.10
class Laser:
    def does(self):
        return 'disitegrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return ('Laser is %s, Claw is %s, SmartPhone is %s' % (
            self.laser.does(), self.claw.does(), self.smartphone.does()))


r = Robot()

print(r.does())
