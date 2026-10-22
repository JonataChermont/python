
colors = {
    "none": "\033[m",
    "red": "\033[1;31m"
}

def increase(number=0, percentage=0, formatation=True): #aumentar
    result = number + ((number * percentage) / 100)
    if not formatation:
        return result
    else:
        return coin(result)

def decrease(number=0, percentage=0, formatation=True): #diminuir
    result = number - ((number * percentage) / 100)
    if not formatation:
        return result
    else:
        return coin(result)

def double(number=0, formatation=True): #dobro
    result = number * 2
    if not formatation:
        return result
    else:
        return coin(result)

def half(number=0, formatation=True): #metade
    result = number / 2
    if not formatation:
        return result
    else:
        return coin(result)

def coin(price=0, coin="R$"):
    return f"{coin}{price:.2f}".replace(".", ",")
