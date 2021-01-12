from functools import reduce

print(reduce(lambda a, b: a * b, [n for n in range(100, 1001, 2)], 1))

from math import prod

print(prod([n for n in range(100, 1001, 2)]))
