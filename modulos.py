import math

print(math.sin(0))

from random import uniform

print(uniform(0, 1))

from random import randint as rnd

print(rnd(5,10))

from math import pi, e

lanzamiento = rnd(1,6)
print(lanzamiento)
if lanzamiento < 4:
    print(pi * lanzamiento)
else:
    print(e * lanzamiento)
