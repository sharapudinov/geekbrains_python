while True:
    m = int(input('номер месяца: '))
    if m >= 1 and m <= 12:
        break
dict = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень'}
list = ['зима', 'весна', 'лето', 'осень']
print(dict[m % 12 // 3])
print(list[m % 12 // 3])
