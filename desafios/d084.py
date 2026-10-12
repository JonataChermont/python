
"""
    Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
    a - quantas pessoas foram cadastras;
    b - uma listagem com as pessoas mais pesadas;
    c - uma listagem com as pessoas mais leves.
"""

titulo = 'LISTA COMPOSTA DE DADOS'
print(f'{'═' * len(titulo)}\n{titulo}\n{'═' * len(titulo)}')

pessoas = list()
dado = list()
maior_peso = menor_peso = 0
pessoas_mais_pesadas = list()
pessoas_mais_leves = list()

while True:
    while True:
        novo_nome = str(input('Nome: ')).strip().title()
        if novo_nome and all(i.isalpha() or i.isspace() for i in novo_nome):
            dado.append(novo_nome)
            break
        print('Nome inválido!')
           
    while True:
        try:
            novo_peso = float(input('Peso: '))
            dado.append(novo_peso)
            break
        except ValueError:
            print('Peso inválido!')

    if len(pessoas) == 0:
        maior_peso = dado[1]
        menor_peso = dado[1]
    else:
        if dado[1] > maior_peso:
            maior_peso = dado[1]
        if dado[1] < menor_peso:
            menor_peso = dado[1]

    pessoas.append(dado[:])
    dado.clear()    
    
    while True:
        continuar = str(input('Quer continuar ? [S/N]: ')).strip().upper()
        if continuar in ('S', 'N'):
            break
        print('Opção inválida! Digite S ou N.')
    if continuar == 'N':
        break

for i in pessoas:
    if i[1] == maior_peso:
        pessoas_mais_pesadas.append(i[0])
    elif i[1] == menor_peso:
        pessoas_mais_leves.append(i[0])

print(f'{'═' * len(titulo)}')
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso:.1f}Kg. Peso de {', '.join(map(str, pessoas_mais_pesadas))}.')
print(f'O menor peso foi de {menor_peso:.1f}Kg. Peso de {', '.join(map(str, pessoas_mais_leves))}.')

