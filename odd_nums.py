def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield print(num)


odd_to_15 = odd_nums(15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
