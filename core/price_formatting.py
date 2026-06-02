
def price_formatting(number):      #str
    n = int(float(number))
    formatted = f"{n:,}".replace(",", " ")
    return formatted
