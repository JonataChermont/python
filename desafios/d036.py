
# escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
# salário ou então o empréstimo será negado.
print('APROVANDO EMPRESTIMO')

valor_casa = float(input('Valor da casa: '))
salario_comprador = float(input('Salário do comprador: '))
anos_financiamento = int(input('Quantos anos de financiamento ? '))
prestacao = valor_casa / (anos_financiamento * 12)
limite_prestacao = (salario_comprador * 30) // 100
print(f'Para pagar uma casa de {valor_casa:.2f} em {anos_financiamento} anos a prestação será de R${prestacao:.2f}')
if prestacao > limite_prestacao:
  print('Empréstimo NEGADO!')
else:
  print('Empréstimo APROVADO!')