def odd_nums(n):
    for i in range(1, n, 2):
        yield i


odd_to_15 = odd_nums(15)
print(next(odd_to_15), end=' ')
print(next(odd_to_15), end=' ')
print(next(odd_to_15), end=' ')
print(next(odd_to_15), end=' ')
print(next(odd_to_15), end=' ')
print(next(odd_to_15), end=' ')
print(next(odd_to_15))


nums_gen = (num for num in range(1, 15, 2))
print(*nums_gen)

