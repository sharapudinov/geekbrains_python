my_list =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(*[my_list[i] for i in range(1, len(my_list)) if my_list[i] not in my_list[:i]+my_list[i+1:]])
