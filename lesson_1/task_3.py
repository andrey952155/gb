"""Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
"""

for el in list(range(1, 100)):
    if 10 < el < 20 or str(el)[-1] in ['5', '6', '7', '8', '9', '0']:
        print(str(el), 'процентов')
    else:
        if str(el)[-1] == '1':
            print(el, 'процент')
        elif str(el)[-1] in ['2', '3', '4']:
            print(el, 'процента')
