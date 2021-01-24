class Cell:
    def __init__(self, cells):
        self.__cels = cells

    def __add__(self, other):
        return Cell(self.__cels + other.__cels)

    def __sub__(self, other):
        sub = Cell(self.__cels - other.__cels)
        if sub <= 0:
            print('Недопустимая операция, нельзя вичитать из большей клетки меньшую')
            raise ArithmeticError
        return sub

    def __mul__(self, other):
        return Cell(self.__cels * other.__cels)

    def __truediv__(self, other):
        div = Cell(self.__cels // other.__cels)
        if div == 0:
            print('Недопустимая операция, нельзя вичитать из большей клетки меньшую')
            raise ArithmeticError
        return div

    def make_order(self, width: int):
        return ('*' * width + '\n') * (self.__cels // width) + '*' * (self.__cels % width)


cell = Cell(8)
cell1 = cell * cell

print(cell1.make_order(7))
