def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))


unicode_test('A')

unicode_test('$')

unicode_test('\u00a2')

unicode_test('\u20ac')

unicode_test('\u2603')

place = 'café'
place

import unicodedata

unicodedata.name('\u00e9')

unicodedata.lookup('E WITH ACUTE, LATIN SMALL LETTER')

unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')

place = 'caf\u00e9'
place

place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
place

u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
u_umlaut

drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'in a', place)

len('$')

len('\U0001f47b')

snowman = '\u2603'

len(snowman)

ds = snowman.encode('utf-8')

len(ds)

ds

ds = snowman.encode('ascii')

snowman.encode('ascii', 'ignore')

snowman.encode('ascii', 'replace')

snowman.encode('ascii', 'backslashreplace')

snowman.encode('ascii', 'xmlcharrefreplace')

place = 'caf\u00e9'
place

type(place)

place_bytes = place.encode('utf-8')
place_bytes

type(place_bytes)

place2 = place_bytes.decode('utf-8')
place2

place3 = place_bytes.decode('ascii')

place4 = place_bytes.decode('latin-1')
place4

place5 = place_bytes.decode('windows-1252')
place5

'%s' % 42

'%d' % 42

'%x' % 42

'%o' % 42

'%s' % 7.03

'%f' % 7.03

'%e' % 7.03

'%g' % 7.03

'%d%%' % 100

actor = 'Richard Gere'
cat = 'Chester'
weight = 28

"My wife's favorite actor is %s" % actor

"Our cat %s weighs %s pounds" % (cat, weight)

n = 42
f = 7.03
s = 'string cheese'

'%d %f %s' % (n, f, s)

'%10d %10f %10s' % (n, f, s)

'%-10d %-10f %-10s' % (n, f, s)

'%10.4d %10.4f %10.4s' % (n, f, s)

'%.4d %.4f %.4s' % (n, f, s)

'%*.*d %*.*f %*.*s' % (10, 4, n, 10, 4, f, 10, 4, s)

'{} {} {}'.format(n, f, s)

'{2} {0} {1}'.format(f, s, n)

'{n} {f} {s}'.format(n=42, f=7.03, s='string cheese')

d = {'n': 42, 'f': 7.03, 's': 'string cheese'}

'{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other')

'{0:d} {1:f} {2:s}'.format(n, f, s)

'{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese')

'{0:10d} {1:10f} {2:10s}'.format(n, f, s)

'{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s)

'{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s)

'{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s)

'{0:>10.4d} {1:>10.4f} {2:10.4s}'.format(n, f, s)

'{0:!^20s}'.format('BIG SALE')

import re

result = re.match('You', 'Young Frankenstein')

youpattern = re.compile('You')

result = youpattern.match('Young Frankenstein')

import re

source = 'Young Frankenstein'
m = re.match('You', source)  # match starts at the beginning of source
if m:  # match returns an object; do this to see what matched
    print(m.group())

m = re.match('^You', source)  # start anchor does the same
if m:
    print(m.group())

m = re.match('Frank', source)
if m:
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.match('.*Frank', source)
if m:  # match returns an object
    print(m.group())

m = re.search('Frank', source)
if m:  # search returns an object
    print(m.group())

m = re.findall('n', source)
m  # findall returns a list

print('Found', len(m), 'matches')

m = re.findall('n.', source)
m

m = re.findall('n.?', source)
m

m = re.split('n', source)
m  # split returns a list

m = re.sub('n', '?', source)
m  # sub returns a string

import string

printable = string.printable
len(printable)

printable[0:50]

printable[50:]

re.findall('\d', printable)

re.findall('\w', printable)

re.findall('\s', printable)

x = 'abc' + '-/*' + '\u00ea' + '\u0115'

re.findall('\w', x)

source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''

re.findall('wish', source)

re.findall('wish|fish', source)

re.findall('^wish', source)

re.findall('^I wish', source)

re.findall('fish$', source)

re.findall('fish tonight.$', source)

re.findall('fish tonight\.$', source)

re.findall('[wf]ish', source)

re.findall('[wsh]+', source)

re.findall('ght\W', source)

re.findall('I (?=wish)', source)

re.findall('(?<=I) wish', source)

re.findall('\bfish', source)

re.findall(r'\bfish', source)

m = re.search(r'(. dish\b).*(\bfish)', source)
m.group()

m.groups()

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
m.group()

m.groups()

m.group('DISH')

m.group('FISH')

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
the_bytes

the_byte_array = bytearray(blist)
the_byte_array

b'\x61'

b'\x01abc\xff'

the_bytes[1] = 127

the_byte_array = bytearray(blist)
the_byte_array

the_byte_array[1] = 127
the_byte_array

the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))

the_bytes

import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

data[16:20]

data[20:24]0x9a

0x9a

0x8d

import struct
struct.pack('>L', 154)

struct.pack('>L', 141)

struct.unpack('>2L', data[16:24])

struct.unpack('>16x2L6x', data)

from construct import Struct, Magic, UBInt32, Const, String
# adapted from code at https://github.com/construct
fmt = Struct('png',
    Magic(b'\x89PNG\r\n\x1a\n'),
    UBInt32('length'),
    Const(String('type', 4), b'IHDR'),
    UBInt32('width'),
    UBInt32('height')
    )
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
result = fmt.parse(data)
print(result)

print(result.width, result.height)

import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_png_header))

print(binascii.unhexlify(b'89504e470d0a1a0a'))
