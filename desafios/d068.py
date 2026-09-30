
"""
    Faça um programa que jogue par ou ímpar com o computador. O jogo
    só será interrompido quando o jogador PERDER, mostrando o total
    de vitórias consecutivas que ele no final do jogo.
"""
from random import randint
titulo = 'VAMOS JOGAR PAR OU ÍMPAR'
print(f'{'=' * len(titulo)}\n{titulo}\n{'=' * len(titulo)}')

jogada_player = 0
jogada_computador = 0
escolha_player = ''
soma = 0
resultado = ''
vitorias = 0

while True:
    jogada_player = int(input('Jogue um valor: '))
    escolha_player = str(input('Par ou Ímpar ? [P/I]: ')).strip().upper()
    jogada_computador = randint(0, 9)
    soma = jogada_player + jogada_computador
    if soma % 2 == 0:
        resultado = 'PAR'
       
    else:
        resultado = 'ÍMPAR'
        
    print('=' * len(titulo))
    print(f'Voçê jogou {jogada_player} e o computador jogou {jogada_computador}. Total de {soma} é {resultado}')
    print('=' * len(titulo))

    if resultado == 'PAR' and escolha_player == 'P' or resultado == 'ÍMPAR' and escolha_player == 'I':
        vitorias += 1
        print('Voçê VENCEU!')
        print('Vamos Jogar novamente...')
        print('=' * len(titulo))
    else:
        print('Voçê PERDEU!')
        print('=' * len(titulo))
        break

print(f'GAMER OVER! Voçê venceu {vitorias} vezes.')
