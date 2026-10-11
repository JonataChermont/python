
"""
    Crie um programa onde o usuário possa digitar vários valores
    numéricos e cadastre-os em uma lista. Caso o número já exista
    lá dentro, ele não será adicionado. No final, serão exibidos
    todos os valores únicos digitados, em ordem crescente.
"""

titulo = 'VALORES ÚNICOS EM UMA LISTA'
borda = "═" * 33
print(f"╔{borda}╗")
print(f"║{titulo:^33}║")
print(f"╚{borda}╝")

numeros = list()
novo_numero = int(input('Digite um valor: '))
numeros.append(novo_numero)
continuar = input('Quer continuar ? [S/N]: ').strip().upper()

while True:
    while continuar not in 'SN':
        continuar = input('Quer continuar ? [S/N]: ').strip().upper()
    else:
        if 'N' in continuar:
            break
        else:
            novo_numero = int(input('Digite um valor: '))
            while novo_numero in numeros:
                print('Valor duplicado! Não vou adcionar')
                novo_numero = int(input('Digite um valor: '))
            else:
                numeros.append(novo_numero)
                continuar = input('Quer continuar ? [S/N]: ').strip().upper()

print('═' * 35)
print(f'Voçê digitou os números {', '.join(map(str, numeros))}.')