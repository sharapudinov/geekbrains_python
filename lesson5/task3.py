from functools import reduce

with open('solary') as f:
    solary = dict(tuple(line.split()) for line in f)
    print('низкооплачевыемые сотрудники:', *[name for name, sol in solary.items() if int(sol) < 20])
    print(f'средняя ЗП {reduce(lambda a, b: float(a) + float(b) / len(solary), solary.values(),0)}')
