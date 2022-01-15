class Stationery:
    """ сделано неправильно - не нужно переопределять метод, если в нём только super"""

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pencil(Stationery):

    def draww(self):
        print('Запуск отрисовки. Используем ', self.title)


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки. Используем ', self.title)


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки. Используем ', self.title)


pencil = Pencil('карандаш')
handle = Handle('маркер')
pen = Pen('ручка')

pencil.draw()
handle.draw()
pen.draw()
