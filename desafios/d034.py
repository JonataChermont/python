
# escreva um programa que pergunte o salário de um fúncionario e
# calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
print('AUMENTOS MÚLTIPLOS')

salario = int(input('Qual é o salário do fúncionario ? R$'))
salario_com_aumento = 0
aumento_salario_menor_igual_1250 = 15
aumento_salario_maior_1250 = 12

if salario <= 1250:
  salario_com_aumento = salario + (salario * aumento_salario_menor_igual_1250) // 100
  print(f'Quem ganhava R${salario}, com o aumento de 15%, passa a ganhar R${salario_com_aumento} agora.')
else:
  salario_com_aumento = salario + (salario * aumento_salario_maior_1250) // 100
  print(f'Quem ganhava R${salario}, com o aumneto de 12%, passa a ganhar R${salario_com_aumento} agora.')
  