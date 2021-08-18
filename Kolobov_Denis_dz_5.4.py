src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [
    el
    for el in src[1:]
    if el > src.pop(0)]
print(result)
