class Date:
    def __init__(self, date: str):
        date = Date.get(date)
        if not Date.validate(**date):
            raise ValueError
        self.date = date

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
        if days_in_month[month] < day or day < 0:
            print(f'В этом месяце не может быть {day}-е число')
            return False
        return True

    def __str__(self):
        return str(self.date)


print(Date('31-09-061'))

print(Date.validate(day=29, month=2, year=2000))
