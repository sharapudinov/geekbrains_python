from json import dump
from statistics import mean

with open('companies.txt', 'r') as f:
    analytic = {line.split()[0]: float(line.split()[2]) - float(line.split()[3]) for line in f}
    analytic['avg_profit'] = mean(filter(lambda a: a>=0,analytic.values()))
    print(analytic)

with open('analytic.json', 'w') as f:
    dump(analytic, f)
