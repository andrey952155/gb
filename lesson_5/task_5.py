import timeit
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result_1 = [el for el in src if src.count(el) == 1]
print('Первый способ решения', result_1)

result_2 = (el for el in src if src.count(el) == 1)
print('Второй способ решения', list(result_2))


"""Ниже замеряем время выполнения каждой из программ 100 000 раз,
    чтобы цифры были не очень маленькие"""
code_list = """
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [el for el in src if src.count(el) == 1]
"""
code_set = """
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result2 = (el for el in src if src.count(el) == 1)
"""
time_list = timeit.timeit(code_list, number=100000)
print('Время выполнения первого способа', time_list)
time_set = timeit.timeit(code_set, number=100000)
print('Время выполнения вторго способа', time_set)
