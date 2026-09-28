
"""
    Crie um programa que leia o ano de nascimento de sete pessoas.
    No final, mostre quantas pessoas ainda não atingiram a maioridade
    e quantas já são maiores.
"""
from datetime import date
print('GRUPO DA MAIORIDADE')

ano_atual = date.today().year
menor = 0
maior = 0
for i in range(0, 7):
    nascimento = int(input(f'Em que ano a {i+1}ª pessoa nasceu ? '))
    idade = ano_atual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor+= 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
