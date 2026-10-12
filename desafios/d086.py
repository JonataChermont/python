
"""
Crie um programa que crie uma matriz da dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
        ┌───┬───┬───┐
      0 │   │   │   │
        ├───┼───┼───┤
      1 │   │   │   │
        ├───┼───┼───┤
      2 │   │   │   │
        └───┴───┴───┘
          0   1   2
"""
titulo = 'MATRIZ EM PYTHON'
print(f'{'═' * len(titulo)}\n{titulo}\n{'═' * len(titulo)}')

matriz = [[ 0 for i in range(3)] for i in range(3)]

for i in range(0, 3):
    for c in range(0, 3):
        while True:
            try:
                matriz[i][c] = int(input(f'Digite um valor para [{i}, {c}]: '))
                break
            except ValueError:
                print('Número inválido!')


print(f'{'═' * len(titulo)}')
for i in range(3):
    for c in range(3):
        print(f'[{matriz[i][c]:^7}]', end='')
    print()
