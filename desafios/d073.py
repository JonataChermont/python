
"""
    Crie uma tupla preenchida com os 20 primeiros colocados da
    tabela do campeonato brasileiro de futebol, na ordem de colocação.
    Depois mostre:
    a - os primeiros;
    b - os últimos 4 colocados;
    c - times em ordem alfabética;
    d - em que posição está o time da chapecoense.
"""
titulo = "CAMPEONATO BRASILEIRO SÉRIE A"
largura = len(titulo) + 4
borda = "═" * largura
print(f"╔{borda}╗")
print(f"║  {titulo}  ║")
print(f"╚{borda}╝")

times = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Santos', 'Coritiba', 'Bragantino', 'São Paulo', 'Botafogo', 'EC Vitória', 'Corinthians', 'Mirassol', 'Vasco da Gama', 'Grêmio', 'Internacional', 'Remo', 'Chapecoense')

print('Tabela do brasileirão séria A 2026 - rodada 28 de 38')
for i in range(0, len(times)):
    if i >= 0 and i <= 8:
        print(f'0{i + 1} - {times[i]}')    
    else:
        print(f'{i + 1} - {times[i]}')
print(borda)

print(f'Os 5 primeiros times são {times[0:5]}')
print(borda)

print(f'Os 4 últimos são {times[-4:]}')
print(borda)

print(f'Times em ordem alfabética {tuple(sorted(times))}')
print(borda)

print(f'A Chapecoense está na {times.index('Chapecoense') + 1}ª posição')
