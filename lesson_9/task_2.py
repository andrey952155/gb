class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self):
        return self._width * self._length * 25 * 5


road_one = Road(100, 6)
print(road_one.calc_weight())
