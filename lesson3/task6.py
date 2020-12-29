def my_func(str):
    return chr(ord(str[0]) - ord('a') + ord('A')) + str[1:]


def main():
    print(*(my_func(i) for i in input('введите строку слов латинницей ').split()))


main()
