
"""
    Faça um programa que calcule a soma entre todos
    os números ímpares que são multíplos de três e que
    se encontram no intervalo de 1 até 500.
"""
print('SOMA ÍMPARES MÚLTIPLOS DE TRÊS')
soma = 0
valores = 0

for i in range(1, 500, 2):
    if i % 3 == 0:
        print(i)
        valores += 1
        soma += i

print(f'A soma de todos os {valores} valores solicitados é de {soma}')
