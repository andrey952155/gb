def num_translate(word):
    dc = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
          'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if word[0].isupper():
        result = dc.get(word[0].lower() + word[1:])
        if result is not None:
            return result.upper()[0] + result[1:]
    return dc.get(word)


print(num_translate('One'))
