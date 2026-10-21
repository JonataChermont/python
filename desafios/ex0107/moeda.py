
colors = {
    "none": "\033[m",
    "red": "\033[1;31m"
}

def number_validation(msg="Digite um número: "):
    while True:
        try:
            number = float(input(msg))
            return number
        except ValueError:
            print(f"{colors['red']}Valor inválido!{colors['none']}")

def increase(number, percentage): #aumentar
    return number + ((number * percentage) / 100)

def decrease(): #diminuir
    pass

def double(number): #dobro
    return number * 2

def half(number): #metade
    return number / 2
