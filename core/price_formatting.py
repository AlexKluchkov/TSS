
def price_formatting(number):      #str
    n = float(number.replace(",", "."))
    formatted = f"{n:,.2f}".replace(",", "X").replace(".", ",").replace("X", " ")
    return formatted
