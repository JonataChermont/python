
"""
    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep

from funcoes_globais import titulo

titulo("FUNÇÃO QUE DESCOBRE O MAIOR", "=")

def maior(*numero):
    print("-=-" * 18)
    print("Analisando os valores passados...")
    for i in numero:
        print(i, end=" ", flush=True)
        sleep(0.5)
    if len(numero) == 0:
        print("Foram informados 0 valores ao todo.")
        print("Não teve um número para ser o maior!")
    else:
        print(f"Foram informados {len(numero)} valores ao todo.")
        print(f"O maior valor informado foi {max(numero)}.")

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
