
"""
    Elabore um programa que calcule o valor a ser pago por produto,
    considerando o seu preço normal e condição de pagamento:
    - à vista dinheiro/cheque: 10% de desconto
    - à vista no cartão: 5% de desconto
    - em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros
"""
print(f'{'='*10}GERENCIADOR DE PAGAMENTOS{'='*10}')

preco_compra = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção ? '))
a_vista_dinheiro = preco_compra - (preco_compra * 10) // 100
a_vista_cartao = preco_compra - (preco_compra * 5) // 100
duas_vezes_cartao = preco_compra
tres_vezes_ou_mais_cartao = preco_compra + (preco_compra * 20) // 100

if opcao == 1:
    print(f'Sua compra de R${preco_compra:.2f} vai custar R${a_vista_dinheiro:.2f} no final.')
elif opcao == 2:
    print(f'Sua compra de R${preco_compra:.2f} vai custar R${a_vista_cartao:.2f} no final.')
elif opcao == 3:
    print(f'Sua compra de R${preco_compra:.2f} vai custar R${duas_vezes_cartao:.2f} no final.')
elif opcao == 4:
    parcela = int(input('Quantas parcelas ? '))
    preco_parcelado = tres_vezes_ou_mais_cartao / parcela
    print(f'Sua compra será parcelada em {parcela}x de R${preco_parcelado:.2f} COM JUROS')
    print(f'Sua compra de R${preco_compra:.2f} vai custar R${tres_vezes_ou_mais_cartao:.2f} no final.')
else:
    print('Opção inválida!')
