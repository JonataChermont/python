
#escreva uma programa que faça o computador "pensar" em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
#pelo computador. O programa deverá escrever na tela se usuário venceu ou perdeu.
from time import sleep
from random import randint
titulo = 'JOGO DA ADIVINHAÇÃO'
mensagem = 'Vou pensar em um número entre 0 e 5. Tente adivinhar'
print(f'{'='*(len(mensagem)//2 - len(titulo)//2)}{titulo}{'='*(len(mensagem)//2 - len(titulo)//2)}')
print(f"""{'='*len(mensagem)}
{mensagem}
{'='*len(mensagem)}""")

numero = randint(0, 5)
print(numero)
tentativa = int(input('Em que número eu pensei ? '))
print('PROCESSANDO...')

sleep(2)
if tentativa == numero:
  print(f'PARABÉNS! Eu estava pensando no número {tentativa}')
else:
  print(f'GANHEI! Eu pensei no número {numero}!')
