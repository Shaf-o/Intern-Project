from forex_python.converter import CurrencyRates
from decimal import Decimal

c = CurrencyRates()

while True:
    amount = input('Enter Amout: ')
    try:
        amount = Decimal(amount)
    except ValueError:
        print('Enter amount in Numbers:')
        continue

    from_crun = input('From Currency: ').upper()
    to_crun = input("To Currency: ").upper()

    result = c.convert(from_crun, to_crun, amount)
    print(from_crun, "to", to_crun,":" ,amount)
    print(result)
