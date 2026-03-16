# fuction that extracts the currecy symbol from a given string
def extract_currency_symbol(price):
    return price[0] if not price[0].isdigit() else "No symbol found"
print(extract_currency_symbol("$100"))
print(extract_currency_symbol("$250"))
print(extract_currency_symbol("100"))

#bunu anlamadim