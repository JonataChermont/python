
# Escreva um programa qu leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
print('COMPARANDO NÚMEROS')

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

if primeiro_numero > segundo_numero:
  print('O primeiro número é MAIOR!')
elif primeiro_numero < segundo_numero:
  print('O segundo número é MAIOR!')
else:
  print('Não existe valor maior, os dois números são IGUAIS!')
