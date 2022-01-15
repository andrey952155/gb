from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args, **kwargs):
        if kwargs:
            print('Именованные аргументы: ', end='')
            print(*(f'{key}: {type(kwargs[key])}' for key in kwargs), sep=', ')
        func = callback(*args, **kwargs)
        print('Позиционные аргументы: ', end='')
        print(*(f'{arg}: {type(arg)}' for arg in args), sep=', ')
        print('Имя переданной функции: ', callback.__name__)
        print(f'Тип значения, возвращенного функцией: {type(func)}')
        return func
    return wrapper


@type_logger
def calc_cube(x):
    return x**3


@type_logger
def demonstration_work(*args, **kwargs):
    """Функция для демонстрации работы декоратора"""
    return args, kwargs


print('Значение возвращенное функцией calc_cube(5): ', calc_cube(5))
print()
demonstration_work(11, 12.00, 'строка', arg_1='text', arg_2=True, arg_3=123)
help(demonstration_work)
