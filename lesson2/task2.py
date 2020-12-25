list = []
while True:
    i = input()
    if i == '`':
        break
    list.append(i)
for i in range(0,len(list)-2,2):
    list[i], list[i+1] = list[i+1], list[i]
print(list)

