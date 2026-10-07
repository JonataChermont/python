
"""
    Desenvolva um programa que leia quatro valores pelo teclado e guade-os
    em uma tupla. No final, mostre:
    a - quantas vezes apareceu o valor 9;
    b - em que posição foi digitado o primeiro valor 3;
    c - quais foram os números pares.
"""

titulo = 'ANÁLISE DE DADOS EM UMA TUPLA'
largura = len(titulo) + 4
borda = "═" * largura
print(f"╔{borda}╗")
print(f"║  {titulo}  ║")
print(f"╚{borda}╝")

numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
pares = []

print('Voçê digitou os números:', *numeros)
print(f'O valor 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado')

for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
print(f'Os valores pares digitados foram', *tuple(pares))