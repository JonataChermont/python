
"""
    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
    a - de 1 até 10, de 1 em 1;
    b - de 10 até 0, de 2 em 2;
    c - uma contagem personalizada.
"""

from time import sleep

from funcoes_globais import titulo

titulo("FUNÇÃO DE CONTADOR", "-")

def linha():
    print("-=" * 20)

def contador(inicio, fim, passo):
    linha()
    print(f"contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        for i in range(inicio - 1, fim, passo):
            print(i+1, end=" ", flush=True)
            sleep(0.5)
    else:
        for i in range(inicio, fim-1, passo):
            print(i, end=" ", flush=True)
            sleep(0.5)
    print("FIM!")

def validacao_dados(texto):
    while True:
        try:
            valor = int(input(texto))
            return valor
        except ValueError:
            print("Valor inválido!")

contador(1, 10, 1)
contador(10, 0, -2)
print("Agora é a sua vez de personalizar a contagem!")
contador(
    validacao_dados("Início: "),
    validacao_dados("Fim: "),
    validacao_dados("Passo: ")
)
