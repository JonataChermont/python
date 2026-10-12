
"""
    Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, crie duas listas extras que vão conter apenas os valores
    pares e os valores ímpares digitados, respectivamente. Ao final, mostre
    o conteúdo das três listas geradas.
"""

titulo = 'DIVIDINDO VALORES EM VÁRIAS LISTAS'
print(f'{'═' * len(titulo)}\n{titulo}\n{'═' * len(titulo)}')

lista = []
lista_par = []
lista_impar = []

while True:
    while True:
        try:
            novo_numero = int(input('Digite um número inteiro: '))
            break
        except ValueError:
            print('Número inválido! Digite um número INTEIRO')

    if novo_numero in lista:
        print('Valor duplicado! Não vou adcionar')
    else:
        lista.append(novo_numero)
        if novo_numero % 2 == 0:
            lista_par.append(novo_numero)
        else:
            lista_impar.append(novo_numero)

    while True:
        continuar = str(input('Quer continuar ? [S/N]: ')).strip().upper()
        if continuar in ('S', 'N'):
            break
        print('Opção inválida! Digite apenas S ou N.')
    if continuar == 'N':
        break

lista.sort()
lista_par.sort()
lista_impar.sort()

print(f'{'═' * len(titulo)}')
print(f'A lista completa é {' → '.join(map(str, lista))}.')

if lista_par:
    print(f'A lista de pares é {' → '.join(map(str, lista_par))}.')
else:
    print('Voçê não digitou números pares!')
    
if lista_impar:
    print(f'A lista de ímpares é {' → '.join(map(str, lista_impar))}.')
else:
    print('Voçê não digitou números ímpares!')
