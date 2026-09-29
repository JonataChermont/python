
"""
    Escreva um programa que leia um número "n" inteiro qualquer e
    mostre na tela os "n" primeiros elementos de uma sequência de Fibonacci.
    Ex:
    0 → 1 → 1 → 2 → 3 → 5 → 8
"""

titulo = 'SEQUÊNCIA DE FIBONACCI'
print(f'{'-' * len(titulo)}\n{titulo}\n{'-' * len(titulo)}')

numero_termos = int(input('Digite quantos termos voçê quer mostrar: '))
termo_atual = 0
termo_antecessor = 1
contador = 1

while contador <= numero_termos:
    print(f'{termo_atual} → ', end='')
    termo_atual += termo_antecessor
    termo_antecessor = termo_atual - termo_antecessor
    contador += 1

print('FIM')
