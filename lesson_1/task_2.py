"""Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X)"""
ls = [str(i ** 3) for i in list(range(1, 1000, 2))]


""" Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
    Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
    Внимание: использовать только арифметические операции! """
result = []
for i in ls:
    summa = sum([int(number) for number in list(i)])
    if summa % 7 == 0:
        result.append(int(i))
print(sum(result))


""" К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
    сумма цифр которых делится нацело на 7. """
result_b = []
ls = [int(integer) + 17 for integer in ls]
ls = list(map(str, ls))
for i in ls:
    summa = sum([int(number) for number in list(i)])
    if summa % 7 == 0:
        result_b.append(int(i))
print(sum(result_b))


""" * Решить задачу под пунктом b, не создавая новый список. """
result_c2 = 0
for i in range(1, 1000, 2):
    i = (i ** 3) + 17
    integer2 = i
    i = str(i)
    i = list(i)
    i = list(map(int, i))
    i = sum(i)
    if i % 7 == 0:
        result_c2 = result_c2 + integer2
print(result_c2)
