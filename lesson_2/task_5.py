def prices_format(ls, reverse):
    ls.sort(reverse=reverse)
    for key, price in enumerate(ls):
        price = float(price)
        ls[key] = f'{str(price).split(".")[0]} руб {str(price).split(".")[1].zfill(2)} коп'
    return ls


prices = [57.8, 46.51, 97, 36.17, 42, 53.11, 5.90, 77.12, 28.05]
prices_up = prices.copy()

print('_________')
print('Адрес списка в памяти  до изменнеия', id(prices))
print('Цены по возрастанию:', prices_format(prices, False))
print('Адрес списка в памяти после изменнеия', id(prices))
print('_________')
prices_up = prices_format(prices_up, True)
print('Цены по убыванию', prices_up)
print('_________')
print('Пять самых дорогих цен по возрастанию: ', prices_up[:5][::-1])
print('_________')
