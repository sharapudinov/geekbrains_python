def div(a, b):
    if b == 0:
        print('Error: division by zero')
        return
    return a / b


def main():
    while True:
        try:
            a = float(input('делимое = '))
            break
        except:
            continue
    while True:
        try:
            b = float(input('делитель = '))
            break
        except:
            continue

    print(f'a/b = {div(a, b)}')


main()
