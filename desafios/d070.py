
"""
    Crie um programa que leia o nome eo preço de vários produtos.
    O programa deverá perguntar se o usuário vai continuar. No final, mostre:
    - qual é o total gasto na compra;
    - quantos produtos custam mais de R$1000;
    - qual é o nome do produto mais barato.
"""

titulo = 'LOJA SUPER DESCONTO'
print(f'{'=' * len(titulo)}\n{titulo}\n{'=' * len(titulo)}')

mais_mil = 0
soma = 0
contador = 0
preco_mais_barato = 0
nome_mais_barato = ' '

while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    contador += 1
    soma += preco

    if contador == 1 or preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = produto

    if preco > 1000:
        mais_mil += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N]')).strip().upper()
    if 'N' in continuar:
        break

print(' FIM DO PROGRAMA '.center(30, '-'))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {mais_mil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {nome_mais_barato} que custa {preco_mais_barato:.2f}')
