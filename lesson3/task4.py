def my_func(x, y):
    """возведение в целую степень"""
    result = 1;
    p = abs(y)
    while p > 0:
        result *= x
        p -= 1
    return result if y > 0 else 1 / result


from functools import reduce


def my_func_pro(x, y):
    """возведение в целую степень в одну строку"""
    return 1 / my_func_pro(x, -y) if y < 0 else reduce(lambda x, y: x * y, [x for i in range(y)], 1)


def main():
    while True:
        try:
            x = float(input('x = '))
            break
        except:
            print('нужно вещественное число')
            continue
    while True:
        try:
            y = int(input('y = '))
            # по условию показатель отрицательный
            if y < 0:
                break
            else:
                print('нужно отрицательное число')
        except:
            print('нужно целое отрицательное число')
            continue

    print(my_funk_pro(x, y))
    print(my_funk_pro(1, 0))


main()
