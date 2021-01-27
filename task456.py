class Store(dict):
    def income(self, equipment, quantity: int):
        if not type(quantity) is int or quantity < 0:
            raise ValueError
        self[equipment] = self.get(equipment, 0) + quantity

    def outcome(self, equipment, quantity: int):
        if not type(quantity) is int or quantity < 0 or quantity > self[equipment]:
            raise ValueError
        self[equipment] = self.get(equipment, 0) - quantity

    def __str__(self):
        return str(dict([(str(key), value) for key, value in self.items()]))


class Equipment():
    def __init__(self, name: str, price: float):
        self._name = name
        self.price = price
        self._type = 'Equipment'

    def __str__(self):
        return f'{self._type} {self._name}. Price {self.price}'


class Printer(Equipment):
    def __init__(self, name: str, price: float, color: bool):
        self._color = color
        super().__init__(name, price)
        self._type = 'Printer'

    def __str__(self):
        return super().__str__() + f' Color {"yes" if self._color == True else "not"}'


class Scanner(Equipment):
    def __init__(self, name: str, price: float, dpi: int):
        self._dpi = dpi
        super().__init__(name, price)
        self._type = 'Scanner'

    def __str__(self):
        return super().__str__() + f' DPI {self._dpi}'


scanner = Scanner('Xerox', 243.434, 766)

printer = Printer('HP', 983, True)

store = Store()

store.income(equipment=printer, quantity=200)
store.income(equipment=scanner, quantity=1200)
print(store)
try:
    store.outcome(equipment=printer, quantity=90)
    store.outcome(equipment=scanner, quantity=1900)
except ValueError:
    print('недопустимое значение')
print(store)
