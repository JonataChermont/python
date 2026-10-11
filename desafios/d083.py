
"""
    Crie um programa ondeo usuário digite uma expressão qualquer
    que use parênteses. Seu aplicativo deverá analisar se a expressão
    passada está com os parênteses abertos e fechados na ordem correta.
"""

titulo = 'VALIDANDO EXPRESSÕES MATEMÁTICAS'
print(f'{'═' * len(titulo)}\n{titulo}\n{'═' * len(titulo)}')

expressao = input('Digite a expressão: ').strip().lower()
pilha = []
for i in expressao:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada')
