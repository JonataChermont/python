
"""
    faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from time import sleep
from random import randint

titulo = 'JOGA NA MEGA SENA'
print('-' * (len(titulo) + 13))
print(f'{titulo:^30}')
print('-' * (len(titulo) + 13))

jogos = list()
temporaria = list()

while True:
    try:
        jogo = int(input('Quantos jogos você quer que eu sorteie ? '))
        for i in range(0, jogo):
            for c in range(0, 6):
                temporaria.append(randint(1, 60))
            jogos.append(temporaria[:])
            temporaria.clear()
        break
    except ValueError:
        print('Valor inválido!')
        
print('-' * 6, f'SORTEANDO {jogo} JOGOS', '-' * 6)
for i in range(0, jogo):
    sleep(0.8)
    print(f'Jogo {i+1}: {jogos[i]}')
print('-' * 7, '< BOA SORTE! >', '-' * 7)
