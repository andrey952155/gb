import sys

price = sys.argv
if len(price) > 1:
    price = str(price[1]) + '\n'
    with open('bakery.csv', 'a', encoding='utf-8') as file:
        file.write(price)
    print('Добавлено:', price)
else:
    print('Введите сумму')
