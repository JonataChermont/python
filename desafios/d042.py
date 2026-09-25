

"""
 Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de
 mostrar que tipo de triângulo será formado:
 - Equilátero: todos os lados iguais
 - Isósceles: dois lados iguais
 - Escaleno: todos os lados diferentes
"""
print('ANALISANDO TRIÂNGULOS')

primeiro_segmento = int(input('Primeiro segmento: '))
segundo_segmento = int(input('Segundo segmento: '))
terceiro_segmento = int(input('Terceiro segmento: '))

if primeiro_segmento + segundo_segmento > terceiro_segmento and primeiro_segmento + terceiro_segmento > segundo_segmento and segundo_segmento + terceiro_segmento > primeiro_segmento:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if primeiro_segmento == segundo_segmento == terceiro_segmento:
        print('EQUILÁTERO')
    elif primeiro_segmento != segundo_segmento != terceiro_segmento:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
