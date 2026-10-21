
def factorial(num):
    fac = 1
    for i in range(1, num + 1):
        fac *= i
    return fac

def number_validation():
    while True:
        number = input("Digite um número: ")
        if number.isnumeric():
            number = int(number)
            return number
        else:
            print("\033[1;31mValor inválido!\033[m")

def double(number):
    return number * 2

def triple(number):
    return number * 3
