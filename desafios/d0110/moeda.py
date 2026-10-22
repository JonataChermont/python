
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

def summary(price=0, _increase=10, _decrease=12):
    title = "RESUMO DO VALOR"
    print(f"{"-" * (len(title) * 2)}\n{title.center(len(title) * 2)}\n{"-" * (len(title) * 2)}")
    print(f"Preço analisado: \t{coin(price)}")
    print(f"Dobro do preço: \t{double(price)}")
    print(f"Metade do preço: \t{half(price)}")
    print(f"{_increase}% de aumento: \t{increase(price, _increase)}")
    print(f"{_decrease}% de redução: \t{decrease(price, _decrease)}")
    print("-" * (len(title) * 2))
