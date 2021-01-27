class DivisionByZeroException(Exception):
    def __init__(self, text):
        self.txt = text


class float(float):
    def __truediv__(self, other):
        if other == 0:
            raise DivisionByZeroException('Деление на ноль')
        return super().__truediv__(other)


x = float(input('float x = '))
y = float(input('float y ='))

try:
    print(x / y)
except DivisionByZeroException as err:
    print(err)
