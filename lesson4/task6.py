from itertools import count, cycle


def counter(start, stop):
    for i in count(start):
        if i > stop:
            break
        else:
            print(i)


def list_iterator(mi_list, step_count):
    counter = count(0)
    for i in cycle(mi_list):
        if next(counter) >= step_count:
            break
        print(i)


counter(5, 10)
list_iterator([1, 2, 3], 2)
