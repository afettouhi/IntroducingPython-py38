# 7.1
import unicodedata
import re
import binascii
import struct

mystery = '\U0001f4a9'

mystery

name = unicodedata.name(mystery)

name

# 7.2
pop_bytes = bytes(mystery.encode('utf-8'))
pop_bytes

# 7.3
pop1 = pop_bytes
pop_string = pop1.decode('utf-8')
pop_string

# 7.4
text = '''My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s'''

print(text % ('roast beef', 'ham', 'head', 'clam'))

# 7.5
letter = '''
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}'''

# 7.6
response = {'salutation': 'salutation', 'name': 'name', 'product': 'product', 'verbed': 'verbed', 'room': 'room',
            'amount': 'amount', 'animals': 'animals', 'percent': 'percent', 'spokesman': 'spokesman',
            'job_title': 'job_title'}

print(letter.format(**response))

# 7.7
mammoth = '''We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.'''

# 7.8
pat = r'\bc\w*'
re.findall(pat, mammoth)

# 7.9
pat_4 = r'\bc\w{3}\b'
re.findall(pat_4, mammoth)

# 7.10
pat_r = r'\b\w*r\b'
re.findall(pat_r, mammoth)

# 7.11
pat_aeiou = r'\b\w*[aeiou]{3}[^aeiou]\w*\b'
re.findall(pat_aeiou, mammoth)

pat_aeiou_s = r'\b\w*[aeiou]{3}[^aeiou\s]\w*\b'
re.findall(pat_aeiou_s, mammoth)

pat_aeiou_s = r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b'
re.findall(pat_aeiou_s, mammoth)

# 7.12
hex_str = '47494638396101000100800000000000ffffff21f9' + \
    '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hex_str)
print(gif)

# 7.13
gif[:6] == b'GIF89a'

# 7.14
width, height = struct.unpack('<HH', gif[6:10])

width, height
