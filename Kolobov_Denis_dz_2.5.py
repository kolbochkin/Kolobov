example = [47.1, 7.0, 34.8, 55.0, 21.7, 16.0, 59.9, 32.99, 42.17, 34.67, 56.34, 67.87, 24.33, 37.55]
# задание А
for i in example:
    _rubles, _penny = str(i).split('.')
    print(f'{_rubles} руб {int(_penny):02d} коп')

# задание В
print(id(example))
example.sort()
print(id(example))
print(example)
for i in example:
    _rubles, _penny = str(i).split('.')
    print(f'{_rubles} руб {int(_penny):02d} коп')

# задание С
decrease = example.copy()
decrease.reverse()
print(decrease)
# задание D
example.reverse()
five = example[:5]
for i in five:
    _rubles, _penny = str(i).split('.')
    print(f'{_rubles} руб {int(_penny):02d} коп')

