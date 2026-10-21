
"""
    Faça um mini-sistema que utilize o interactive helpp do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar "FIM", o programa se encerrará.
"""

from funcoes_globais import titulo

color = {
    "none": "\033[m",
    "black": "\033[7;30",
    "red": "\033[1;31m",
    "blue": "\033[1;34m",
    "purple": "\033[1;35m"
}

print(color["blue"])
titulo("SISTEMA DE AJUDA PyHELP", "=")
print(color["none"])

def caption(text):
    print(f"{"-" * len(text)}\n{text}\n{"-" * len(text)}")

while True:
    while True:
        entry = str(input("Função ou biblioteca > ").strip().lower())
        if entry and all(i.isalpha() or i.isspace() for i in entry):
            break
        else:
            print("Valor inválido")
    
    if entry == "fim":
        print(color["red"])
        caption("até logo")
        print(color["none"])
        break

    print(color["purple"])
    caption(f"Acessando o manual do comando '{entry}'.")
    print(color["none"])

    print(color["black"])
    help(entry)
    print(color["none"])
