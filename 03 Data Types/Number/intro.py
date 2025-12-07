"""
int
float
complex

type() -> for seeing data types

"""

#int
x = 20
print(x)
print(type(x))

#float
y = 20.0
print(y)
print(type(y))

#complex
z = 10j
print(z)
print(type(z))


#type conversion

print(type(float(x)))
print(type(int(y)))
print(type(complex(y)))


#random number

import random

print(random.randrange(1,10))
