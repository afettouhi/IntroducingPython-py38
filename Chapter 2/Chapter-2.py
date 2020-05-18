a = 7
print(a)

b = a
print(b)

type(a)

type(b)

type(58)

type(99.9)

type('abc')

5

0

05

123

+123

-123

5 + 9

100 - 7

4 - 10

5 + 9 + 3

4 + 3 - 2 - 1 + 6

5+9   +      3

6 * 7

7 * 6

6 * 7 * 2 * 3

9 / 5

9 // 5

5 / 0

7 // 0

a = 95
a

a - 3

a

a = a -3
a

a = 95
temp = a - 3
a = temp

a = a - 3

a = 95
a -= 3
a

a += 8
a

a *= 2
a

a /= 3
a

a = 13
a //= 4
a

9 % 5

divmod(9,5)

9 // 5

9 % 5

2 + 3 * 4

2 + 3 * 4

2 + (3 * 4)

10

0b10

0o10

0x10

int(True)

int(False)

int(98.6)

int(1.0e4)

int('99')

int('-23')

int('+12')

int(12345)

int('99 bottles of beer on the wall')

int('')

int('98.6')

int('1.0e4')

4 + 7.0

True + 2

False + 5.0

googol = 10**100
googol

googol * googol

float(True)

float(False)

float(98)

float('99')

float('98.6')

float('-1.5')

float('1.0e4')

'Snap'

"Crackle"

"'Nay,' said the naysayer."

'The rare double quote in captivity: ".'

'A "two by four" is actually 1 1⁄2" × 3 1⁄2".'

"'There's the man that shot my paw!' cried the limping hound."

'''Boom!'''

"""Eek!"""

poem =  '''There was a Young Lady of Norway,
Who casually sat in a doorway;
When the door squeezed her flat,
She exclaimed, "What of that?"
This courageous Young Lady of Norway.'''

poem = 'There was a young lady of Norway,

poem2 = '''I do not like thee, Doctor Fell.
    The reason why, I cannot tell.
    But this I know, and know full well:
    I do not like thee, Doctor Fell.
'''
print(poem2)

poem2

print(99, 'bottles', 'would be enough.')

''

""

''''''

""""""

bottles = 99
base = ''
base += 'current inventory: '
base += str(bottles)
base

str(98.6)

str(1.0e4)

str(True)

palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
print(palindrome)

print('\tabc')

print('a\tbc')

print('ab\tc')

print('abc\t')

testimony = "\"I did nothing!\" he said. \"Not that either! Or the other thing.\""
print(testimony)

fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105'"
print(fact)

speech = 'Today we honor our friend, the backslash: \\.'
print(speech)

'Release the kraken! ' + 'No, wait!'

"My word! " "A gentleman caller!"

a = 'Duck.'
b = a
c = 'Grey Duck!'
a + b + c

print(a, b, c)

start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)

letters = 'abcdefghijklmnopqrstuvwxyz'
letters[0]

letters[1]

letters[-1]

letters[-2]

letters[25]

letters[5]

letters[100]

name = 'Henny'
name[0] = 'P'

name = 'Henny'
name.replace('H', 'P')

'P' + name[1:]

letters = 'abcdefghijklmnopqrstuvwxyz'

letters[:]

letters[20:]

letters[10:]

letters[12:15]

letters[-3:]

letters[18:-3]

letters[-6:-2]

letters[::7]

letters[4:20:3]

letters[19::4]

letters[:21:5]

letters[-1::-1]

letters[::-1]

letters[-50:]

letters[-51:-50]

letters[:70]

letters[70:71]

len(letters)

empty = ""
len(empty)

todos = 'get gloves,get mask,give cat vitamins,call ambulance'
todos.split(',')

todos.split()

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)

poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

poem[:13]

len(poem)

poem.startswith('All')

poem.endswith('That\'s all, folks!')

word = 'the'
poem.find(word)

poem.rfind(word)

poem.count(word)

poem.isalnum()

setup = 'a duck goes into a bar...'

setup.strip('.')

setup.capitalize()

setup.title()

setup.upper()

setup.lower()

setup.swapcase()

setup.center(30)

setup.ljust(30)

setup.rjust(30)

setup.replace('duck', 'marmoset')

setup.replace('a ', 'a famous ', 100)

setup.replace('a', 'a famous', 100)
