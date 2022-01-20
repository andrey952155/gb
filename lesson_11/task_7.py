class ComplexNumbers:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return f'Результат сложения: {self.number + other.number}'

    def __mul__(self, other):
        return f'Результат умножения: {self.number * other.number} '


a = ComplexNumbers(2 + 2j)
b = ComplexNumbers(3 + 3j)
print(a + b)
print(a * b)
