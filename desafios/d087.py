
"""
    Aprimore o desafio anterior, mostrando no final:
    a - a soma de todos os valores pares digitados;
    b - a soma dos valores da terceira coluna;
    c - o maior valor da segunda linha.
"""

titulo = 'MATRIZ EM PYTHON'
print(f'{'═' * len(titulo)}\n{titulo}\n{'═' * len(titulo)}')

matriz = [[ 0 for i in range(3)] for i in range(3)]
par = []

for i in range(0, 3):
    for c in range(0, 3):
        while True:
            try:
                matriz[i][c] = int(input(f'Digite um valor para [{i}, {c}]: '))
                if matriz[i][c] % 2 == 0:
                    par.append(matriz[i][c])
                break
            except ValueError:
                print('Número inválido!')


print(f'{'═' * len(titulo)}')

for i in range(3):
    for c in range(3):
        print(f'[{matriz[i][c]:^7}]', end='')
    print()

print(f'{'═' * len(titulo)}')

total_par = 0
for i in par:
    total_par += i
print(f'A soma dos valores pares é {total_par}')

terceira_coluna = 0
for i in matriz:
    terceira_coluna += i[2]
print(f'A soma dos valores da terceira coluna é {terceira_coluna}.')

print(f'O maior valor da segunda linha é {max(matriz[1])}.')
    