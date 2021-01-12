#!/usr/bin/env python
def salary(rate, hours, prize):
    return float(rate) * float(hours) + float(prize)


from sys import argv

script, rate, hours, prize = argv

print(salary(rate, hours, prize))


