
# A confederação nacional de natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre a sua categoria,
# de acordo com a idade:
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# até 25 anos: SÊNIOR
# acima: MASTER
from datetime import date
print('CLASSIFICANDO ATLETAS')

ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f'O atleta tem {idade} anos.')

if idade >= 0 and idade <= 9:
  print('Classificação: MIRIM')
elif idade >= 10 and idade <= 14:
  print('Classificação: INFANTIL')
elif idade >= 15 and idade <= 19:
  print('Classificação: JUNIOR')
elif idade > 20 and idade <= 25:
  print('Classificação: SÊNIOR')
elif idade > 25:
  print('Classificação: MASTER')
else:
  print('Classificação: INVÁLIDA')
