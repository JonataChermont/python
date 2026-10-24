
colors = {
    "none": "\033[m",
    "red": "\033[1;31m",
    "green": "\033[32m",
    "blue": "\033[34m"
}

def read_integer(msg="Digite um número inteiro: "):
    while True:
        try:
            number = int(input(msg))
        except:  # noqa: E722
            print(f"{colors['red']}ERRO: por favor, digite um número inteiro válido!{colors['none']}")
        else:
            return number

def name_validation(msg="Nome: "):
    while True:
        while True:
            name = str(input(msg).strip().title())
            if name and all(i.isalpha() or i.isspace() for i in name):
                return name
            else:
                print(f"{colors['red']}Nome inválido{colors['none']}")

def header(text, lin="="):
    print(line(lin))
    print(text.center(42))
    print(line(lin))

def line(line="-", size=42):
    return line * size

def menu(list):
    header("MENU PRINCIPAL", "=")
    for pos, item in enumerate(list):
        print(f"{colors['blue']}{pos + 1}{colors['none']} - {item}")
    print(line())
    option = read_integer("Sua opção: ")
    return option
