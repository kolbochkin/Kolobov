from requests import get
from decimal import *


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    y = response.text.split('>')
    z = False
    for i in range(len(y)):
        if y[i].startswith(currency.upper()) == True:
            z = True
            print(round(Decimal(y[i+6][:6].replace(',', '.')), 2))
    if z == False:
        print('None')
