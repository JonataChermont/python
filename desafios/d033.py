
# faça um programa que leia três números e
# mostre qual é o maior e qual é o menor
print('MAIOR E MENOR VALOR')

primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))
terceiro_numero = int(input('Terceiro número: '))
menor_numero = 0
maior_numero = 0

if primeiro_numero < terceiro_numero and segundo_numero < terceiro_numero:
  maior_numero = terceiro_numero
else:
  menor_numero = terceiro_numero

if primeiro_numero < segundo_numero and terceiro_numero < segundo_numero:
  maior_numero = segundo_numero
else:
  menor_numero = segundo_numero

if segundo_numero < primeiro_numero and terceiro_numero < primeiro_numero:
  maior_numero = primeiro_numero
else:
  menor_numero = primeiro_numero

print(f'O menor número digitado foi {menor_numero}')
print(f'O maior número digitado foi {maior_numero}')
