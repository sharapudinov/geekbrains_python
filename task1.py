class Date:

    @classmethod
    def get(cls, date: str):
        keys = ['day', 'month', 'year']
        return dict([(key, int(value)) for key, value in zip(keys, date.split('-'))])

    @staticmethod
    def validate(*args, day: int, month: int, year: int):
        if 12 < month or month < 1:
            print('месяц должеен быть числом от 1-12')
            return False
        days_in_month = [None, 31, 28 + int(not year % 4), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if days_in_month[month] < day  or day < 0:
            print(f'В этом месяце не может быть {day}-е число')
            return False
        return True


print(Date.get('01-01-01'))

print(Date.validate(day=29, month=2, year=2000))
