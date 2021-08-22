def main(argv):
    program, *args = argv
    txt = []
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            txt.append(line.replace('\n', ''))
    if len(args) == 1:
        for i in range(int(args[0]) - 1, len(txt)):
            print(txt[i])
    elif len(args) == 2:
        for i in range(int(args[0]) - 1, int(args[1])):
            print(txt[i])
    else:
        for i in range(0, len(txt)):
            print(txt[i])

    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
