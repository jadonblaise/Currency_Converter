# Currency Exchange
'''
This code uses the CurrencyRates class from the forex_python.converter module to get exchange rate data.
It takes inputs of amount, from_currency and to_currency. Then it uses the convert method of class object
to convert the amount from one currency to another.
'''
from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = float(input("Enter amount: "))
from_currency = input("Enter from which currency: ")
to_currency = input("Enter to which currency: ")

converted_amount = c.convert(from_currency, to_currency, amount)
print(round(converted_amount, 2))
