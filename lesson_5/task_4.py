from itertools import islice
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for i in range(len(src) - 1):
    a, b = tuple((islice(src, i, i+2, None)))
    if a < b:
        result.append(b)
print(result)