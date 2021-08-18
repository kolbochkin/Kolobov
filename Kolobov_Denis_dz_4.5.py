from requests import get
from decimal import *


def main(argv):
    currency = argv
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    y = response.text.split('>')
    z = False
    for i in range(len(y)):
        if y[i].startswith(str(currency[1]).upper()):
            z = True
            print(round(Decimal(y[i + 6][:6].replace(',', '.')), 2))
    if not z:
        print('None')


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
