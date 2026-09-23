
# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é hora de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print('ALISTAMENTO MILITAR')

ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento
print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')

if idade < 18:
  print(f'Ainda faltam {18 - idade} anos para o alistamento.')
  print(f'Seu alistamento será em {(18 - idade) + ano_atual}.')
elif idade > 18:
  print(f'Voçê já deveria ter se alistado há {idade - 18} anos.')
  print(f'Seu alistamento foi em {ano_atual - (idade - 18)}.')
else:
  print('Voçê tem que se alistar IMEDIATAMENTE!')
