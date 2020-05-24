import math

math.pi

math.e

math.fabs(98.6)

math.fabs(-271.1)

math.floor(98.6)

math.floor(-271.1)

math.ceil(98.6)

math.ceil(-271.1)

math.factorial(0)

math.factorial(1)

math.factorial(2)

math.factorial(3)

math.factorial(10)

math.log(1.0)

math.log(math.e)

math.log(8, 2)

math.pow(2, 3)

2 ** 3

2.0 ** 3

math.sqrt(100.0)

math.sqrt(-100.0)

x = 3.0
y = 4.0
math.hypot(x, y)

math.sqrt(x * x + y * y)

math.sqrt(x ** 2 + y ** 2)

math.radians(180.0)

math.degrees(math.pi)

# a real number
5

# an imaginary number
8j

# an imaginary number
3 + 2j

1j * 1j

(7 + 1j) * 1j

x = 10.0 / 3.0
x

from decimal import Decimal

price = Decimal('19.99')
tax = Decimal('0.06')
total = price + (price * tax)
total

from fractions import Fraction

Fraction(1, 3) * Fraction(2, 3)

Fraction(1.0 / 3.0)

Fraction(Decimal('1.0') / Decimal('3.0'))

import fractions

fractions.gcd(24, 16)

import numpy as np

b = np.array([2, 4, 6, 8])
b

b.ndim

b.size

b.shape

import numpy as np

a = np.arange(10)
a

a.ndim

a.shape

a.size

a = np.arange(7, 11)
a

a = np.arange(7, 11, 2)
a

f = np.arange(2.0, 9.8, 0.3)
f

g = np.arange(10, 4, -1.5, dtype=np.float)
g

a = np.zeros((3,))
a

a.ndim

a.shape

a.size

b = np.zeros((2, 4))
b

b.ndim

b.shape

b.size

import numpy as np

k = np.ones((3, 5))
k

m = np.random.random((3, 5))
m

a = np.arange(10)
a

a = a.reshape(2, 5)
a

a.ndim

a.shape

a.size

a = a.reshape(5, 2)
a

a.ndim

a.shape

a.size

a.shape = (2, 5)
a

a = a.reshape(3, 4)

a = np.arange(10)
a[7]

a[-1]

a.shape = (2, 5)
a

a[1, 2]

l = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
l

l[1, 2]

l[1][2]

a = np.arange(10)
a = a.reshape(2, 5)
a

a[0, 2:]

a[-1, :3]

a[:, 2:4] = 1000
a

from numpy import *

a = arange(4)
a

a *= 3
a

plain_list = list(range(4))
plain_list

plain_list = [num * 3 for num in plain_list]
plain_list

from numpy import *

a = zeros((2, 5)) + 17.0
a

import numpy as np

coefficients = np.array([[4, 5], [1, 2]])
dependents = np.array([20, 13])

answers = np.linalg.solve(coefficients, dependents)
answers

4 * answers[0] + 5 * answers[1]

1 * answers[0] + 2 * answers[1]

product = np.dot(coefficients, answers)
product

np.allclose(product, dependents)
