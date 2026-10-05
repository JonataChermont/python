
"""
    Crie um programa que simule o funcionamento de um caixa eletrônico.
    No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
    e o programa vai informar quantas cédulas de cada valor serão entregues.
    OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

titulo = 'BANCO MASTER DIN'
print(f'{'==' * len(titulo)}\n{titulo:-^32}\n{'==' * len(titulo)}')

valor_saque = int(input('Que valor voçê quer sacar ? R$'))
nota_cinquenta = 50
contador_ciquenta = 0
nota_vinte = 20
contador_vinte = 0
nota_dez = 10
contador_dez = 0
nota_um = 1
contador_um = 0

while True:
    contador_ciquenta = valor_saque // nota_cinquenta
    valor_saque = valor_saque % nota_cinquenta
    contador_vinte = valor_saque // nota_vinte
    valor_saque = valor_saque % nota_vinte
    contador_dez = valor_saque // nota_dez
    valor_saque = valor_saque % nota_dez
    contador_um = valor_saque // nota_um
    valor_saque = valor_saque % nota_um
    if valor_saque < 1:
        break

if contador_ciquenta > 0:
    print(f'Total de {contador_ciquenta} cédulas de R$50')

if contador_vinte > 0:
    print(f'Total de {contador_vinte} cédulas de R$20')

if contador_dez > 0:
    print(f'Total de {contador_dez} cédulas de R$10')

if contador_um > 0:
    print(f'Total de {contador_um} cédulas de R$1')

print(f'{'==' * len(titulo)}\nVolte sempre ao {titulo}')
