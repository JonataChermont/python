
"""
    Melhore o DESAFIO 061, perguntando para o usuário se ele quer
    mostrar mais alguns termos. O programa encerra quando ele disser
    que quer mostrar 0 termos. 
"""
print('GERADOR DE PA')
print('=' * len('GERADOR DE PA'))

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
limite = 1
contador = 10

while limite <= 10:
    print(f'{termo} → ', end='')
    termo += razao
    limite += 1
print('PAUSA')

mais_termos = int(input('Quantos termos voçê quer mostrar a mais ? '))

while mais_termos != 0:
    limite_usuario = 1
    while limite_usuario <= mais_termos:
        print(f'{termo} → ', end='')
        termo += razao
        limite_usuario += 1
        contador += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos voçê quer mostrar a mais ? '))

print(f'Progresso finalizado com {contador} termos mostrados.')
