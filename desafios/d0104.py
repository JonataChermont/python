
"""
    Crie um programa que tehnha a função leia_int(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico.
    Ex:
        n = leiaInt("Digite um n")
"""

from funcoes_globais import titulo

titulo("VALIDANDO ENTRADA DE DADOS")

def leia_int(num):
    while True:
        entrada = input(num)
        if entrada.isnumeric():
            entrada = int(entrada)
            return entrada
        else:
            print("\033[1;31mERRO! Digite um número inteiro válido.\033[0m")


numero = leia_int("Digite um número: ")
print(f"Voçê acabou de digitar o número \033[1;34m{numero}\033[0m.")
