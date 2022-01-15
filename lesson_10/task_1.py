class Matrix:

    def __init__(self, new_matrix):
        self.matrix = new_matrix

    def __str__(self):
        return f'{self.matrix}'

    def __add__(self, other):
        result = []
        for i, j in zip(self.matrix, other.matrix):
            result.append([x + y for x, y in zip(i, j)])
        return result


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(a, b)
print(a + b)
