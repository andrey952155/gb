import abc
from abc import ABC

"""Cell"""


class Clothes(ABC):

    all_cloth = 0

    @abc.abstractmethod
    def calc(self):
        pass


class Costume(Clothes):

    def __init__(self, h):
        self.h = int(h)
        Clothes.all_cloth += self.calc

    @property
    def calc(self):
        cloth = 2 * self.h + 0.3
        return cloth

    def __str__(self):
        return f'Для пальто размером {self.h} потребуется {self.calc} ткани.' \
               f' Всего израсходовано {Clothes.all_cloth} ткани'


class Coat(Clothes):

    def __init__(self, v):
        self.v = int(v)
        Clothes.all_cloth += self.calc

    @property
    def calc(self):
        cloth = self.v / 6.5 + 0.5
        return cloth

    def __str__(self):
        return f'Для пальто размером {self.v} потребуется {self.calc} ткани.' \
               f' Всего израсходовано {Clothes.all_cloth} ткани'


cos_1 = Costume(50)
print(cos_1)
cos_2 = Costume(52)
print(cos_2)
cos_3 = Costume(54)
print(cos_3)
coat_1 = Costume(172)
print(coat_1)
coat_2 = Costume(174)
print(coat_2)
coat_3 = Costume(176)
print(coat_3)

