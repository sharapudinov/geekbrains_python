def my_funk(x, y):
    """возведение в целую степень"""
    result = 1;
    p = abs(y)
    while p > 0:
        result *= x
        p -= 1
    return result if y > 0 else 1 / result


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

    print(my_funk(x, y))


main()
