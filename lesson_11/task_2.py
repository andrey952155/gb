class OwnError(Exception):
    pass


input_a = input('Введите первое число: ')
input_b = input('Введите второе число: ')
try:
    input_a = float(input_a)
    input_b = float(input_b)
    if input_b == 0:
        raise OwnError('На 0 делить нельзя!')
except ValueError:
    print('Введите число!')
except OwnError as err:
    print(err)
else:
    print(input_a / input_b)
