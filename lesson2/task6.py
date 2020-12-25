catalog=[]
index = 1
while True:
    name = input('название: ')
    if name == '`':
        break
    while True:
        price = int(input('цена: '))
        if price >=0:
            break
        print('цена должна быть натуральным числом')
    while True:
        quantity =int(input('количество: '))
        if quantity>=0:
            break
        print('количество должно быть натуральным числом')
    unit =input('ед: ')
    catalog.append((index,{'название': name,'цена': price,'количество':quantity,'ед':unit}))
    index+=1
analitic = {}
for product in catalog:
    for prop in product[1].keys():
        prop_set=analitic.get(prop,set())
        prop_set.add(product[1][prop])
        analitic[prop] = prop_set
for prop in analitic.keys():
    analitic[prop] = list(analitic.get(prop))

print(analitic)