
"""
    Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crecente.
"""

titulo = 'LISTAS COM PARES E ÍMPARES'
print(f'{'═' * len(titulo)}\n{titulo}\n{'═' * len(titulo)}')

valores = [[], []]

for i in range(0, 7):
    while True:
        try:
            novo_valor = int(input(f'Digite o {i+1}° valor: '))
            if novo_valor in valores[0] or novo_valor in valores[1]:
                print('Este valor já foi digitado!')
                continue

            if novo_valor % 2 == 0:
                valores[0].append(novo_valor)
            else:
                valores[1].append(novo_valor)
            break
        except ValueError:
            print('Número inválido!')

valores[0].sort()
valores[1].sort()

print(f'{'═' * len(titulo)}')
print(f'Os valores pares digitados foram: {' → '.join(map(str, valores[0])) or 'nenhum'}.')
print(f'Os valores ímpares digitados foram: {' → '.join(map(str, valores[1])) or 'nenhum'}.')
