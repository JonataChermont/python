
"""
    Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada patida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

titulo = "CADASTRO DE JOGADOR DE FUTEBOL"
print(f"{"=" * (len(titulo) * 2)}\n{titulo:^45}\n{"=" * (len(titulo) * 2)}")

jogador = {}
gols = []
total_gols = 0

jogador["nome"] = str(input("Nome do jogador: ")).strip().title()
partidas = int(input(f"Quantas partidas {jogador["nome"]} jogou ? "))

for i in range(partidas):
    gols.append(int(input(f"Quantos gols na {i+1}ª partida: ")))

jogador["gols"] = gols.copy()
for i in gols:
    total_gols += i
jogador["total"] = total_gols

print(f"{"-=" * len(titulo)}\n{jogador}\n{"-=" * len(titulo)}")
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("-=" * len(titulo))
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for num, i in enumerate(gols):
    print(f"    => Na {num + 1}ª partida, fez {i} gols.")
print(f"Foi um total de {total_gols} gols.")
