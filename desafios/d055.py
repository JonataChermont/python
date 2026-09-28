
"""
    Faça um programa que leia o peso de cinco pessoas.
    No final, mostre qual foi o maior e o menor peso lidos.
"""
print('MAIOR E MENOR DA SEQUÊNCIA')

menor = 0
maior = 0
for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    

print(f'O Maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')