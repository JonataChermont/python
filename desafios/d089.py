
"""
    Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

titulo = 'BOLETIM ESCOLAR'
print(f'{'-' * (len(titulo) * 2)}\n{titulo:^30}\n{'-' * (len(titulo) * 2)}')

alunos = []
dados = []
media = 0

while True:
    while True:
        novo_nome = str(input('Nome: ')).strip().title()
        if novo_nome and all(i.isalpha() or i.isspace() for i in novo_nome):
            dados.append(novo_nome)
            break
        print('Nome inválido!')

    for i in range(1, 3):
        while True:
            try:
                nota = float(input(f'Nota {i}: '))
                if nota >= 0 and nota <= 10:
                    dados.append(nota)
                    break
                else:
                    print('Nota Inválida')
            except ValueError:
                print('Valor inválido!')

    alunos.append(dados[:])
    dados.clear()

    while True:
        continuar = str(input('Quer continuar ? [S/N]: ')).strip().upper()
        if continuar in ('S', 'N'):
            break
        else:
            print('Digite S ou N')
    if continuar == 'N':
        break

print('-=' * len(titulo))
print(f'{'No.':<9} {'NOME':<9}{'MÉDIA':>9}')
print('-' * (len(titulo) * 2))

for i in range(0, len(alunos)):
    media = (alunos[i][1] + alunos[i][2]) / 2
    print(f'{i:<9} {alunos[i][0]:<9}{media:>9.1f}')

print('-=' * len(titulo))

while True:
    while True:
        try:
            mostar_notas = int(input('Mostrar notas de qual aluno ? (999 interrompe): '))
            for i in range(0, len(alunos)):
                if mostar_notas == i:
                    print(f'Notas de {alunos[i][0]} são: {' e '.join(map(str, alunos[i][1:]))}')
                    print('-=' * len(titulo))
            break
        except ValueError:
            print('Valor Inválido!')
    if mostar_notas == 999:
        break
