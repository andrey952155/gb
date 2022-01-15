class Worker:

    def __init__(self, name, surname, position, **kwargs):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = kwargs


class Position(Worker):

    def __init__(self, name, surname, position, **kwargs):
        super().__init__(name, surname, position, **kwargs)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


worker_one = Position('Иван', 'Иванов', 'дворник', wage=50000, bonus=500)

print(worker_one.get_full_name())
print(worker_one.get_total_income())
