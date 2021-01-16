with open('companies.txt') as f:
    analytic = {line.split()[0]: float(line.split()[2]) - float(line.split()[3]) for line in f}
    analytic['avg_profit'] = sum([value for value in analytic.values() if value > 0], 0)
    print(analytic)
