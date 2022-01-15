from random import choice


def get_jokes(num: int, delete=False) -> list:
    """Функция возвращает список из элементов, случайн овыбранных из трех списков num раз
    Если передать флаг delete=True, возвращенные элементы повторятся не будут"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = []
    for i in range(num):
        random_in_nouns = choice(nouns)
        random_in_adverbs = choice(adverbs)
        random_in_adjectives = choice(adjectives)
        if delete:
            nouns.remove(random_in_nouns)
            adverbs.remove(random_in_adverbs)
            adjectives.remove(random_in_adjectives)
        result.append(f'{random_in_nouns} {random_in_adverbs} {random_in_adjectives}')
    return result


print(get_jokes(3, delete=True))
