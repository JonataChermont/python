
# faça um programa que leia um ano qualquer
# e mostre se ele é bissexto
import datetime
print('ANO BISSEXTO')

ano = int(input('Que ano quer analisar ? Coloque 0 para analisar o ano atual: '))
ano_atual = datetime.datetime.now().year

if ano == 0:
  ano = ano_atual

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'O ano de {ano} é BISSEXTO')
else:
  print(f'O ano de {ano} NÃO é BISSEXTO')

