
"""
    Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, mostre:
    a - quantos números foram digitados;
    b - a lista de valores, ordenada de forma decrescente;
    c - se o valor 5 foi digitado e está ou não na lista.
"""

titulo = 'EXTRAINDO DADOS DE UMA LISTA'
print(f'{'═' * len(titulo)}\n{titulo}\n{'═' * len(titulo)}')

numeros = []
contador = 0

while True:
    while True:
        try:
            novo_numero = int(input('Digite um valor: '))
            break
        except ValueError:
            print('Valor inválido! Tente novamente.')
    numeros.append(novo_numero)
    contador += 1
    continuar = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    else:
        if continuar in 'N':
            break

print(f'{'═' * len(titulo)}')
numeros.sort()
print(f'Voçê digitou {contador} elementos.')
print(f'Os valores em ordem crescente são {' → '.join(map(str, numeros))}.')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')