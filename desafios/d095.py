
"""
    Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
"""
    ENUNCIADO DO DESAFIO 093
    Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada patida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

titulo = "CADASTRO DE JOGADOR DE FUTEBOL"
print(f"{"=" * len(titulo)}\n{titulo}\n{"=" * len(titulo)}")
lista_jogadores = {}
dados_jogador = {}
jogador = []
gols = []
total_gols = 0

while True:
    while True:
        nome = str(input("Nome do jogador: ").strip().title())
        if nome and all(i.isalpha() or i.isspace() for i in nome):
            dados_jogador["nome"] = nome
            break
        else:
            print("Nome inválido")

    while True:
        try:
            partidas = int(input(f"Quantas partidas {dados_jogador["nome"]} jogou ? "))
            if partidas > 0:
                dados_jogador["partidas"] = partidas
                break
            else:
                print("O jogador tem que ter jogado no minímo 1 partida")
        except ValueError:
            print("Valor inválido")

    for i in range(partidas):
        while True:
            try:
                gols_marcados = int(input(f"    Quantos gols na {i+1}ª partida: "))
                if gols_marcados >= 0:
                    gols.append(gols_marcados)
                    break
                else:
                    print("Digite um valor positivo")
            except ValueError:
                print("Valor inválido!")

    for i in gols:
        total_gols += i
    
    dados_jogador["gols"] = gols[:]
    dados_jogador["total"] = total_gols
    gols.clear()
    total_gols = 0

    jogador.append(dados_jogador.copy())

    while True:
        continuar = str(input("Quer continuar ? [S/N]: ").strip().upper())
        if continuar not in ("S", "N"):
            print("ERRO! Digite apenas S ou N.")
        else:
            break
    if continuar == "N":
        break

print("=" * 45)
print(f"{"cod":<4}{"nome":<15}{"partidas":<20}{"gols":<5}")
print("-" * 45)
for cod, j in enumerate(jogador):
    print(f"{cod:<4}{j["nome"]:<15}{j["partidas"]!s:<20}{j["total"]:<5}")
print("-" * 45)    

while True:
    if len(jogador) == 1:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogador[0]["nome"]}:")
        for i, v in enumerate(jogador[0]["gols"]):
            print(f"    No {i+1}º jogo fez {v} gols.")
        break
    while True:
        try:
            levantamento_jogador = int(input("Mostrar dados de qual jogador ? (999 para parar): "))
            if levantamento_jogador == 999:
                break
            if levantamento_jogador >= 0 and levantamento_jogador < len(jogador):
                print(f"-- LEVANTAMENTO DO JOGADOR {jogador[levantamento_jogador]["nome"]}:")
                for i, v in enumerate(jogador[levantamento_jogador]["gols"]):
                    print(f"    No {i+1}º jogo fez {v} gols.")
            else:
                print(f"Digite um valor entre 0 e {len(jogador) - 1}")
        except ValueError:
            print("Valor inválido!")
    break

print("<< VOLTE SEMPRE >>")
