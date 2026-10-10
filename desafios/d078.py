
"""
    Crie um programa que leia 5 valores numéricos e guarde-os em uma lista.
    No final, mostre qual foi o maior e o menor valor digitado e suas respectivas
    posições na lista.
"""

titulo = 'MAIOR E MENOR VALORES NA LISTA'
borda = "═" * 33
print(f"╔{borda}╗")
print(f"║{titulo:^33}║")
print(f"╚{borda}╝")

numeros = list()

for i in range(0, 5):
    numeros.append(int(input(f'Digite um valor inteiro para a posição {i}: ')))

print('═' * 35)

maior = max(numeros)
menor = min(numeros)

print(f'Voçê digitou os valores {', '.join(map(str, numeros))}.')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, i in enumerate(numeros):
    if i == maior:
        print(f'{pos}', end='... ')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for pos, i in enumerate(numeros):
    if i == menor:
        print(f'{pos}', end='... ')
print()
