def user_print(*args, name, surname, year, city, email, phone):
    print(f'Name - {name}, Surname - {surname}, Year - {year}, City - {city}, Email - {email}, Phone - {phone}')


def main():
    name = input('Name: ')
    surname = input('Surname: ')
    while True:
        try:
            year = int(input('Year: '))
            break
        except:
            continue
    city = input('City: ')
    email = input('Email: ')
    phone = input('Phone: ')

    user_print(name=name, surname=surname, year=year, city=city, email=email, phone=phone)


main()
