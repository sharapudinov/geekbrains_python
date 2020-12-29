def my_func(a, b, c):
    return a + b + c - min(a, b, c)


def input_int(output):
    while True:
        try:
            return int(input(output))
        except:
            print('только цифры')
            continue


def main():
    a = input_int('a = ');
    b = input_int('b = ');
    c = input_int('c = ');

    print(my_func(a, b, c))


main()
