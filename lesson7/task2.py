from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Costume(Clothes):
    def __init__(self, H):
        self.__H = H

    @property
    def fabric_consumption(self):
        return 2 * self.__H + 0.3


class Coat(Clothes):
    def __init__(self, V):
        self.__V = V

    @property
    def fabric_consumption(self):
        return self.__V / 6.5 + 0.5


print(Coat(35).fabric_consumption)
print(Costume(1.9).fabric_consumption)
