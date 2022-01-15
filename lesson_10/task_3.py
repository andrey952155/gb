class Cell:

    def __init__(self, particle):
        self.particle = particle

    def __str__(self):
        return str(self.particle)

    def __add__(self, other):
        return f'Сумма ячеек {self.particle + other.particle}'

    def __gt__(self, other):
        return self.particle > other.particle

    def __sub__(self, other):
        if self > other:
            return f'Разница колличества ячеек в клетках {self.particle - other.particle}'
        return f'Во второй клетке ячеек больше чем в первой'

    def __mul__(self, other):
        return f'Произведение ячеек {self.particle * other.particle}'

    def __floordiv__(self, other):
        return f'Деление ячеек {self.particle // other.particle}'

    def make_order(self, len_line):
        line = f'{"*"*len_line}\\n'
        count_line = self.particle // len_line
        end_line = self.particle % len_line
        return f'{line*count_line}{"*"*end_line}'


cell_1 = Cell(22)
cell_2 = Cell(20)
print(f'Колличество ячеек в кдетках {cell_1} и {cell_2}')
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(5))
