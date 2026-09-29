
"""
    Refaça o DESAFIO 051, lendo o primeiro termo
    e a razão de uma PA, mostrando os 10 primeiros
    termos da progressão usando a estrutura while.
"""
print('GERADOR DE PA')
print('=' * len('GERADOR DE PA'))

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
limite = 1

while limite <= 10:
    print(f'{termo} → ', end='')
    termo = termo + razao
    limite += 1

print('FIM')
