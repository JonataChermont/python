

print('AUMENTO SALARIAL')
salario = float(input('Qual é o salário do funcionário ? R$'))
aumento = int(input('Quantos porcentos o salário do funcionário vai aumentar ? R$'))

salario_final = salario + (salario * aumento / 100)

print(f'Um funcionário que ganhava R${salario}, com {aumento}% de aumento, passa a receber R${salario_final:.2f}')

