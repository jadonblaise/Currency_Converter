# 💱 Currency Exchange Converter

A simple Python script that converts an amount from one currency to another using the [`forex-python`](https://pypi.org/project/forex-python/) library.

---

## 📌 Features
- Convert an amount from **any currency** to another in real time.
- Uses the `CurrencyRates` class from `forex_python.converter`.
- Rounds the converted amount to 2 decimal places.

---

## 📦 Requirements
- Python 3.7+
- [forex-python](https://pypi.org/project/forex-python/)

Install the required library with:

```bash
pip install forex-python
```
## ▶️ How to Run
- git clone https://github.com/jadonblaise/Currency_Converter.git
- cd Currency_Converter
-  Save the script as currency_exchange.py.

- Run the script:
  python currency_exchange.py

- Enter:

  Amount to convert
  
  Source currency code (e.g., USD, EUR)
  
  Target currency code (e.g., INR, GBP)

## Example
  Enter amount: 100\
  Enter from which currency: USD\
  Enter to which currency: EUR\
  85.32

## ⚠️ Notes
Currency codes must follow the ISO 4217 standard (e.g., USD, EUR, INR).

Internet connection is required to fetch real-time rates.

The result is rounded to 2 decimal places.
