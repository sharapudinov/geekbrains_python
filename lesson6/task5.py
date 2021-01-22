class Stationery:
    def __init__(self,title):
        self._title = title

    def drow(self):
        print ('Запуск отрисовки')

class Pen(Stationery):
    def drow(self):
        print(f'Pen {self._title}')
        super().drow()


class Pencil(Stationery):
    def drow(self):
        print(f'Pencil {self._title}')
        super().drow()

class Handle(Stationery):
    def drow(self):
        print(f'Handle {self._title}')
        super().drow()



pen = Pen('Erich Crause')

pensil = Pencil('НоуНейм')

handle = Handle('Страдивари')

pen.drow()
pensil.drow()
handle.drow()