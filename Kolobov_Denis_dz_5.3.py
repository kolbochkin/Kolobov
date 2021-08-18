tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
lasses = ['9А', '7В', '9Б', '9В', '8Б'] #, '10А', '10Б', '9А'


def tuple_generator():
    for num in range(0, len(tutors)):
        if num + 1 > len(lasses):
            yield print(tuple([tutors[num], None]))
        else:
            yield print(tuple([tutors[num], lasses[num]]))


z = tuple_generator()
next(z)
next(z)
next(z)
next(z)
next(z)
next(z)
next(z)

