def thesaurus(*args):
    index = {}
    for i in args:
        val = list(filter(lambda el: el.startswith(i[0]), args))
        index.setdefault(i[0], val)
    print(index)


thesaurus("Иван", "Мария", "Петр", "Илья")
