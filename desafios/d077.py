
"""
    Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
    Depois disso, voçê deve mostrar, para cada palavra, quais são as suas vogais.
"""

titulo = 'CONTANDO VOGAIS EM TUPLAS'
borda = "═" * 33
print(f"╔{borda}╗")
print(f"║{titulo:^33}║")
print(f"╚{borda}╝")

palavras = (
    'APRENDER',
    'PROGRAMAR',
    'LINGUAGEM',
    'PYTHON',
    'CURSO',
    'GRATIS',
)

for i in palavras:
    print(f'\nNa palavra {i} temos ', end='')
    for vogal in i.lower():
        if vogal in 'aeiou':
            print(vogal, end=' ')
print()
print(f'\n{'═' * 35}')
