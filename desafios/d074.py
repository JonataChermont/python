
"""
    Crie um programa que vai gerar cinco números aleatórios e colocar
    em uma tupla. Depois disso, mostre a listagem números gerados e também
    indique o menor e o maior valor que estão na tupla.
"""

from random import randint
titulo = 'MAIOR E MENOR VALORES EM TUPLA'
largura = len(titulo) + 4
borda = "═" * largura
print(f"╔{borda}╗")
print(f"║  {titulo}  ║")
print(f"╚{borda}╝")

numeros = (randint(0 , 10), randint(0 , 10), randint(0 , 10), randint(0 , 10), randint(0 , 10))
print('Os valores foram:', *numeros)
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
