import os


def calc_keys(size):
    i = 10
    value_key = 1
    while size != 0:
        size = size // i
        value_key *= 10
    return value_key


result = {}
for file in os.listdir('some_data'):
    key = calc_keys(os.stat(os.path.join('some_data', file)).st_size)
    if result.get(key):
        result[key] += 1
    else:
        result[key] = 1

    """Пытался эту часть кода записать через тернарный оператор
     result[key] = result[key + 1] if result.get(key) else 1
     Но получил ошибку:
     result[key] = result[key] + 1 if result.get(key) else result[key] = 1
                  ^
            SyntaxError: cannot assign to conditional expression
     Было бы интересно посмотреть на правильную запись, или здесь тернарный оператор
     применить нельзя?"""

print(result)
