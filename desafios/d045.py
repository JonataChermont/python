
"""
    Crie um programa que faça o computador jogar jokenpô com voçê.
"""
from random import randint
from time import sleep
print('PEDRA, PAPEL E TESOURA')
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
player = int(input('Qual é a sua jogada ?'))
computador = randint(1, 3)
def jogada(escolha):
    if escolha == 1:
        return 'PEDRA'
    elif escolha == 2:
        return 'PAPEL'
    elif escolha == 3:
        return 'TESOURA'
    else:
        return 'INVÁLIDA'

sleep(0.6)
print('\nJO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('PÔ!!!\n')
print('-=' * 11)
print(f'Computador jogou {jogada(computador)}')
print(f'Jogador jogou {jogada(player)}')
print('-=' * 11)

if player == computador:
    print('EMPATE')
elif player == 1 and computador == 3 or player == 2 and computador == 1 or player == 3 and computador == 2:
    print('JOGADOR VENCEU')
else:
    print('COMPUTADOR VENCEU')
