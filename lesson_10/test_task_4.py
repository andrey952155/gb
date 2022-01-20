class OwnError(Exception):
    pass


ls = []


def update_list(data):
    if data:
        ls.append(data)


def define_type(callback):
    def wrapper(arg):
        try:
            func = callback(arg)
        except ValueError:
            return None
        return func
    return wrapper


@define_type
def data_float(data):
    return float(data)


@define_type
def data_int(data):
    return int(data)


while True:
    dt = input('Введите число: ')
    if dt == 'stop':
        print(ls)
        break
    dt_int = data_int(dt)
    dt_float = data_float(dt)
    update_list(dt_int)
    update_list(dt_float)
    try:
        if not dt_int and not dt_float:
            raise OwnError
    except OwnError:
        print('Не то ввели')

