

"""
    Melhore o jogo do desafio 028 onde o computador vai "pensar"
    em um número entre 0 e 10. Só que agora o jogador vai tentar
    adivinhar até acertar, mostrando no final quantos palpites
    foram necessários para vencer.
"""
from random import randint
print('JOGO DA ADIVINHAÇÃO V2.0')
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que voçê consegue adivinhar qual foi ?''')
palpite = int(input('Qual seu palpite: '))
numero_computador = randint(0, 10)
tentativas = 0

while palpite != numero_computador:
    if palpite < numero_computador:
        print('Mais... Tente mais uma vez.')
    elif palpite > numero_computador:
        print('Menos... Tente mais uma vez.')
    palpite = int(input('Qual seu palpite: '))
    tentativas += 1

print(f'Acertou com {tentativas + 1} tentativas. Parabéns!')
