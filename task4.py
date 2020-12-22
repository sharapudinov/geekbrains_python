n = int(input())
max = 0
while n > 0:
    d = n % 10
    if d > max:
        max = d
    n //= 10
print(max)
