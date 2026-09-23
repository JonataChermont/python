

print('SEPARANDO DIGITOS DE UM NÚMERO')

numero = input('Informe um número: ').strip().replace(' ', '')

print(f'Analisando o número {numero}')
print(f'UNIDADE: {numero[len(numero) - 1]}')
print(f'DEZENA: {numero[len(numero) - 2]}')
print(f'CENTENA: {numero[len(numero) - 3]}')
print(f'MILHAR: {numero[len(numero) - 4]}')

