

print('CALCULANDO DESCONTO')

preco_produto = float(input('Digite o preço do produto: '))
desconto_produto = int(input('Digite o valor do desconto em porcentagem: '))

preco_final = preco_produto - (preco_produto * desconto_produto / 100)

print(f'O produto que custava R${preco_produto}, na promoção com desconto de {desconto_produto}% vai custar R${preco_final:.2f}')


