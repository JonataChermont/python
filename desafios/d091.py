
"""
    Crie um programa onde 4 jogadores joguem uma dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
 
from operator import itemgetter
from random import randint
from time import sleep

titulo = "JOGO DE DADOS"
print(f"{'=' * (len(titulo) * 2)}\n{titulo:^26}\n{'=' * (len(titulo) * 2)}")

jogadores = {
    'jogador1': randint(0, 6),
    'jogador2': randint(0, 6),
    'jogador3': randint(0, 6),
    'jogador4': randint(0, 6)
}

print(f"{"NÚMEROS SORTEADOS":^26}")
for k, v in jogadores.items():
    sleep(0.8)
    print(f"{k} tirou {v} no dado.")

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print(f"{"RANKING DOS JOGADORES":=^26}")
for i, v in enumerate(ranking):
    sleep(0.8)
    print(f"{i+1}ª lugar: {v[0]} com {v[1]}.")
