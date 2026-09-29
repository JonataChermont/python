
"""
    Faça um programa que leia um número qualquer
    e mostre o seu fatorial.
    Ex:
    5! = 5 x 4 x 3 x 2 x 1 = 120
"""
print('CÁLCULO DE FATORIAL')

numero = int(input('Digite um número inteiro\npara calcular seu fatorial: '))
fatorial = 1
print(f'Calculando {numero}! = ', end='')

while numero > 0:
    print(f'{numero}', end='')
    if numero > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fatorial *= numero
    numero -= 1
    
print(f'{fatorial}')