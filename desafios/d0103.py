
"""
    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e qauntos gols ele marcou.  O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

from funcoes_globais import titulo

titulo("FICHA DO JOGADOR", "=")

def token(name="<desconhecido>", goals=0):
    print(f"O jogador {name} fez {goals} gol(s) no campeonato.")

player_name = str(input("Nome do jogador: ").title())
number_goals = str(input("Número de gols: "))

if number_goals.isnumeric():
    number_goals = int(number_goals)
else:
    number_goals = 0

if player_name.strip() == "":
    token(goals=number_goals)
else:
    token(player_name, number_goals)
