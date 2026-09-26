
"""
    Refaça o DESAFIO 09, mostrando a tabuada de um número que usuário
    escolher, só que agora utilizando um laço for.
"""
print('TABUADA')

numero = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    multiplicacao = numero * i
    print(f'{numero} x {i} = {multiplicacao}')
