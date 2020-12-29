def div(a, b):
    if b == 0:
        print('Error: division by zero')
        return
    return a / b


def input_float(output):
    while True:
        try:
            return float(input(output))
        except:
            print('нужно вещественное число')
            continue


def main():
    a = input_float('делимое = ')
    b = input_float('делитель = ')
    print(f'a/b = {div(a, b)}')


main()
