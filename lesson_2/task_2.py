ls = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for value in ls:
    if ls[ls.index(value) - 1] != ' ' and ls.index(value) != 0:
        ls.insert(ls.index(value), ' ')
for key, value in enumerate(ls):
    if value.isdigit() and ls[key - 1] != '"' and ls[key - 1].isdigit() is False:
        ls[key] = f'{int(value):02d}'
        ls.insert(key, '"')
        ls.insert(key + 2, '"')
    elif value.startswith(('+', '-')) and ls[key - 1] != '"':
        ls[key] = f'{value[0]}{int(value):02d}'
        ls.insert(key, '"')
        ls.insert(key + 2, '"')
print(''.join(ls))
