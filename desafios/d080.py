
"""
    Crie um programa onde o usuário possa digitar cinco valores númericos e 
    cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
    No final, mostre a lista ordenada na tela.
"""

titulo = 'LISTA ORDENADA SEM REPETIÇÃO'
print(f'{'═' * len(titulo)}\n{titulo}\n{'═' * len(titulo)}')

valores = []
for i in range(0, 5):
    novo_valor = int(input('Digite um valor: '))
    if i == 0 or novo_valor > valores[-1]:
        valores.append(novo_valor)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(valores):
            if novo_valor <= valores[posicao]:
                valores.insert(posicao, novo_valor)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1

print('═' * len(titulo))
print(f'Os valores digitados em ordem {', '.join(map(str, valores))}.')
