
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
par = 0
impar = 0

while True:
    try:
        novo_numero = int(input('Digite um número inteiro: '))
        lista.append(novo_numero)
        if novo_numero % 2 == 0:
            lista_par.append(novo_numero)
            par += 1
        else:
            lista_impar.append(novo_numero)
            impar += 1
        break
    except ValueError:
        print('Número inválido! Digite um número INTEIRO')

while True:
    continuar = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    else:
        if 'N' in continuar:
            break

    while True:
        try:
            novo_numero = int(input('Digite um número inteiro: '))
            while novo_numero in lista:
                print('Valor duplicado! Não vou adcionar')
                novo_numero = int(input('Digite um valor: '))
            else:
                lista.append(novo_numero)
                if novo_numero % 2 == 0:
                    lista_par.append(novo_numero)
                    par += 1
                else:
                    lista_impar.append(novo_numero)
                    impar += 1
                break
        except ValueError:
            print('Número inválido! Digite um número INTEIRO')

lista.sort()
lista_par.sort()
lista_impar.sort()
print(f'{'═' * len(titulo)}')
print(f'A lista completa é {' → '.join(map(str, lista))}.')
if par > 0:
    print(f'A lista de pares é {' → '.join(map(str, lista_par))}.')
else:
    print('Voçê não digitou números pares!')
if impar > 0:
    print(f'A lista de ímpares é {' → '.join(map(str, lista_impar))}.')
else:
    print('Voçê não digitou números ímpares!')
