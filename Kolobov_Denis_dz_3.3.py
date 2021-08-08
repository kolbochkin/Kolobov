def thesaurus(*args):
    index = {}
    for i in args:
        z = i[0]
        print(z)
        print(index.setdefault(z, i))
    print(index)
    #key = tuple(map(str[0], args)
    #print(f'args: {args}')
    #print(key)


thesaurus("Иван", "Мария", "Петр", "Илья")
