from random import choice


def get_jokes(n=1, flag=0):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    if flag == 0:
        for i in range(n):
            x, y, z = choice(nouns), choice(adverbs), choice(adjectives)
            jokes.append(x + ' ' + y + ' ' + z)
    else:
        for i in range(n):
            x, y, z = choice(nouns), choice(adverbs), choice(adjectives)
            jokes.append(x + ' ' + y + ' ' + z)
            nouns.remove(x)
            adverbs.remove(y)
            adjectives.remove(z)

    print(jokes)


get_jokes(3, 1)
get_jokes(2, 0)
get_jokes(3)
