
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
while True:
    novo_numero = int(input('Digite um valor: '))
    numeros.append(novo_numero)
    for i in range(1, len(numeros)):
        if novo_numero == numeros[i]:
            print('Valor duplicado! Não vou adicionar...')
        else:
            print('Valor adicionado com sucesso...')

    continuar = input('Quer continuar ? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar ? [S/N]: ').strip().upper()
    else:
        if 'N' in continuar:
            print('═' * 35)
            print(f'Voçê digitou os valores {', '.join(map(str, numeros))}.')
            break
