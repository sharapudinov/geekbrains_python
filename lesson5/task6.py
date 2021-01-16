from re import split

with open('lessons.txt') as f:
    print(
        {line.split(': ')[0]: sum([int(i) for i in filter(lambda a: a != '', split(r'\D+', line.split(': ')[1]))]) for
         line in f})

