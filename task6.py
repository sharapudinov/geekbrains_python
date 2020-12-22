a = int(input('a = '));
b = int(input('b = '));

d = 0
while a < b:
    a *= 1.1
    d += 1

print(d)

# правильный способ
import math

print(math.ceil(math.log(b / a, 1.1)))
