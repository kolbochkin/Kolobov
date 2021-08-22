def main(argv):
    program, *args = argv
    txt = args[0] + '\n'
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(txt)

    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
