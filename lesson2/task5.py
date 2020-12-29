my_list = [7, 5, 3, 3, 2]

new = int(input())

for i in range(len(my_list)):
    if i == len(my_list) - 1:
        my_list.append(new)
    elif my_list[i] <= new >= my_list[i + 1]:
        my_list = my_list[:i] + [new] + my_list[i:]
        break
print(my_list)
