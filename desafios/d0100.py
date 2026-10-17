
"""
    Faça programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PAARES sorteados pelo função.
"""

from random import randint
from time import sleep

from funcoes_globais import titulo

titulo("FUNÇÕES PARA SORTEAR E SOMAR", "=")

numeros = []

def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end=" ")
    for i in range(5):
        lista.append(randint(1, 10))
        print(lista[i], end=" ", flush=True)
        sleep(0.3)
    print("FIM!")

def soma_par(lista):
    par = 0
    for i in lista:
        if i % 2 == 0:
            par += i
    print(f"Somando os valores pares de {lista}, temos {par}.")

sorteia(numeros)
soma_par(numeros)
