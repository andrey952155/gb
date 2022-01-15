from time import sleep


class TrafficLight:

    def __init__(self):
        self._color = 'красный'

    def running(self):
        while True:
            print(self._color)
            sleep(7)
            self._color = 'желтый'
            print(self._color)
            sleep(2)
            self._color = 'зеленый'
            print(self._color)
            sleep(4)
            self._color = 'красный'


trafficLight_one = TrafficLight()
trafficLight_one.running()
