
"""
    Crie um programa que tenha uma tupla totalmente preenchida com
    uma contagem por extenso,  de zero até vinte.
    Seu programa deverá ler um número pelo teclado(entre 0 e 20) e
    mostrá-lo por extenso.
"""
from num2words import num2words
print('NÚMERO POR EXTENSO')
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
numero = int(input('Digite um número entre 0 e 20: '))

while numero not in numeros:
    numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
else:
    numero = num2words(numero, lang='pt-br')

print(f'Voçê digitou o número {numero}')