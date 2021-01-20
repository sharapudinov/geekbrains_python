def input_float_line_to_file(filename):
    with open(filename, 'w')  as f:
        while True:
            try:
                x = input('введите чиcло ( "`" для выхода):')
                if x == '`':
                    return
                f.write(f'{float(x)} ')
            except:
                print('нужно число')


if __name__ == '__main__':
    from functools import reduce

    filename = 'file1.txt'
    input_float_line_to_file(filename)
    with open(filename, 'r') as f:
        print(reduce(lambda a, b: float(a) + float(b), f.read().split()))
