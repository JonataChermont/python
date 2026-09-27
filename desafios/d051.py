
"""
    Desenvolva um programa que leia o primeiro termo
    e a razão de uma PA. No final, mostre os 10 primeiros
    termos dessa progressão.
"""
titulo = 'PROGRESSÃO ARITMÉTICA'
subtitulo = '10 TERMOS DE UMA PA'
print(titulo)
print('='* len(titulo))
print(subtitulo.center(len(titulo)))
print('='* len(titulo))

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print(i, end=' ' + '→ ')
print('ACABOU')