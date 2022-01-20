class OwnError(Exception):
    pass


class Store:

    all_product = {}

    def __init__(self):
        self.all_product = Store.all_product


class OfficeEquipment(Store):

    def __init__(self, model, quantity, **kwargs):
        super().__init__()
        self.model = model
        self.quantity = quantity
        self.kwargs = kwargs
        self.all_product[self.model] = {'name': self.model, 'quantity': self.quantity, **self.kwargs}

    def __str__(self):
        kwargs_str = [f"{key} - {self.kwargs[key]}" for key in self.kwargs]
        return f'Модель: {self.model} Количество: {self.all_product[self.model]["quantity"]} {" ".join(kwargs_str)}'

    @classmethod
    def _check_number(cls, number):
        try:
            if type(number) != int:
                raise OwnError
        except OwnError:
            print('Ошибка! Введите целое число!')
        else:
            return True

    def add_product(self, number):
        if OfficeEquipment._check_number(number):
            self.all_product[self.model]['quantity'] += number

    def del_product(self, number):
        if OfficeEquipment._check_number(number):
            self.all_product[self.model]['quantity'] -= number


class Printer(OfficeEquipment):

    def __init__(self, model, quantity, size):
        super().__init__(model, quantity, size=size)


class Scanner(OfficeEquipment):
    def __init__(self, model, quantity, power, price):
        super().__init__(model, quantity, power=power, price=price)


class Xerox(OfficeEquipment):

    def __init__(self, model, quantity, color):
        super().__init__(model, quantity, color=color)


print('Добавим на склад несколько позиций')
xerox = Xerox('xerox-1', 10, 'black')
hp = Scanner('Model_2', 20, '100', '1500')
canon = Printer('Model_3', 30, '300')
print('Посмотрим инфо по опрделенной позиции')
print(hp)
print('Добавим 5 позиций, и посмотрим что получилось')
hp.add_product(5)
print(hp)
print('Удалим две')
hp.del_product(2)
print(hp)
print('Введем при добавлении строку вместо числа')
hp.add_product('10')
print(hp)
