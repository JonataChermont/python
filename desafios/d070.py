
"""
    Crie um programa que leia o nome eo preço de vários produtos.
    O programa deverá perguntar se o usuário vai continuar. No final, mostre:
    - qual é o total gasto na compra;
    - quantos produtos custam mais de R$1000;
    - qual é o nome do produto mais barato.
"""

titulo = 'LOJA SUPER DESCONTO'
print(f'{'=' * len(titulo)}\n{titulo}\n{'=' * len(titulo)}')

produto = str(input('Nome do produto: ')).strip().upper()
preco = float(input('Preço: R$'))
mais_mil = 0
soma = produto
nome_mais_barato = produto
preco_mais_barato = preco

while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    soma += preco
    preco_mais_barato = preco
    nome_mais_barato = produto

    if preco_mais_barato > preco:
        preco_mais_barato = preco

    if preco > 1000:
        mais_mil += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N]')).strip().upper()
    if 'N' in continuar:
        break

print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {mais_mil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {preco_mais_barato}')
