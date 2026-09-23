
# desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não
# formar um triângulo
print('ANALISADOR DE TRIÂNGULOS')

primeiro_segmento = float(input('Primeiro segmento: '))
segundo_segmento = float(input('Segundo segmento: '))
terceiro_segmento = float(input('Terceiro segmento: '))

if primeiro_segmento + segundo_segmento > terceiro_segmento and primeiro_segmento + terceiro_segmento > segundo_segmento and segundo_segmento + terceiro_segmento > primeiro_segmento:
  print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
  print('Os segmentos acima NÃO PODEM triângulo!')
