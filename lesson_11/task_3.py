class OwnError(Exception):
    pass


in_data = None
ls = []
while True:
    in_data = input('Введите число: ')
    try:
        if in_data == 'stop':
            raise OwnError
        in_data = float(in_data)
    except OwnError:
        print(ls)
        break
    except ValueError:
        print('Не то ввели!')
    else:
        ls.append(in_data)
