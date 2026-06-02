

def xpath_validation(offer, path, cast=str, default=None):
    result = offer.xpath(path)
    if not result:
        return default
    try:
        return cast(result[0])
    except:
        return default