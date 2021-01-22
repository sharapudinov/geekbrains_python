from threading import Thread
from time import sleep
from playsound import playsound


class Car:
    """
     Класс определяющий автомобиь разгоняющийся до максимальной скорости и тормозящий до остановки
     в своем потоке. Также возможны повороты повороты вправо и влево
    """

    max_speed = 120

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self._speed = 0
        self._acceleration = 0
        self.__runnig_thread = Thread(target=self.__running)

    def go(self, acceleration: float):
        if acceleration <= 0:
            return
        print(f'{self.name}: - Поееехали!')
        self._acceleration = acceleration
        self.__runnig_thread.start()

    def __running(self):
        while self._speed >= 0:
            self.show_speed()
            self._speed += self._acceleration * 0.1 if self._speed <= Car.max_speed else Car.max_speed
            sleep(0.1)
        self._speed = 0

    def stop(self, braking: float):
        print(f'{self.name}: -тпррру!')
        if braking <= 0:
            return
        self._acceleration = - braking

    def turn(self, direction):
        if direction == 'r':
            print(f'{self.name}: -налево')
        elif direction == 'l':
            print(f'{self.name}: -направо')

    def show_speed(self):
        print(f'{self.name} {self._speed:5.2f}')


class CarWithCC(Car):
    """
         Класс определяющий автомобиь с круизконтролем в параллельном потоке
        """
    speed_limit = 60

    def __init__(self, color, name):
        super().__init__(color, name)
        self._cruiz_control_enable = False
        self._cruiz_control_thread = Thread(target=self._cruiz_control)

    def _cruiz_control(self):
        print('Cruiz control enabled')
        while self._cruiz_control_enable:
            if (__class__.speed_limit - self._speed) / self._acceleration < 0:
                self._acceleration = -self._acceleration
            sleep(0.1)
        print('Cruiz control disabled')

    def go(self, acceleration: float, cruiz_control=False):
        self._cruiz_control_enable = cruiz_control
        super().go(acceleration)
        if cruiz_control:
            sleep(1)
            self._cruiz_control_thread.start()

    def stop(self, braking: float):
        self._cruiz_control_enable = False
        super().stop(braking)


class TownCar(CarWithCC):
    speed_limit = 60


class WorkCar(CarWithCC):
    speed_limit = 40


class SportCar(Car):
    '''
    спорткар
    '''
    max_speed = 500


class PoliceCar(CarWithCC):
    '''
    полицейская машина с сиреной
    '''

    max_speed = 300

    def __init__(self, color, name):
        self._seren_enable = False
        self._seren_tread = Thread(target=self.seren)
        super().__init__(color, name)

    def seren(self):
        '''сирена в своем потоке'''

        #TODO: разобраться с проблемой ModuleNotFoundError: No module named gi

        while self._seren_enable:
            playsound('seren.mp3')

    def go(self, acceleration: float, cruiz_contril=False, seren=False):
        self._seren_enable = True;
        self._seren_tread.start()
        super().go(acceleration)

    def stop(self, braking: float):
        self._seren_enable = False
        super().stop(braking)


''' 
Художественный фильм (блокбастер) 'Опасная погоня'
полицеский бобик преследует вишневую девятку'''

car = TownCar('вишневая', 'девятка')
police_car = PoliceCar('желтый', 'бобик')

car.go(50, True)
police_car.go(70, True, True)
sleep(5)
car.stop(100)
police_car.stop(150)
