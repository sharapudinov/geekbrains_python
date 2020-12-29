def main():
    S = 0
    finish = False
    while not finish:
        str = input('вводите вещественные числа (` - выход)')
        for i in str.split():
            if i == '`':
                finish = True
                break
            else:
                try:
                    S += float(i)
                except:
                    print(f'Warning: {i} not is a float number')
                continue
        print(f'S = {S}')
        continue
    print(f'S = {S}')


main()
