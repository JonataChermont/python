
"""
    Faça um programa que leia um número inteiro e diga se ele é
    ou não um número primo.
"""
print('NÚMEROS PRIMOS')

numero = int(input('Digite um número inteiro: '))
divisivel = 0

for i in range(0, numero + 1):
    i += 1
    if numero % i == 0:
        divisivel += 1
    print(i, end=' ')

print(f'\nO número {numero} foi divisível {divisivel} vezes')
if divisivel > 2:
    print('E por isso ele NÃO É PRIMO!')
else:
    print(f'E por isso ele É PRIMO!')