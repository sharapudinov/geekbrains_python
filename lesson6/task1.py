from time import sleep
from itertools import cycle, count
from threading import Thread


class TrafficLight:
    def switch_thread(self):
        states = [('red', 7), ('yellow', 2), ('green', 5), ('yellow', 2)]
        for state, time in cycle(states):
            self.__color = state;
            sleep(time)

    def running(self):
        x = Thread(target=self.switch_thread)
        x.start()

    def getColor(self):
        return self.__color


light = TrafficLight()
light.running()
for i in range(20):
    sleep(2)
    print(light.getColor())
