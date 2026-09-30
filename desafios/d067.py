
"""
    faça um programa que mostre a tabuada de vários números, um de cada vez,
    para cada valor digitado pelo usuário. O programa será interrompido quando
    o número solicitado for negativo.
"""
print('TABUADA v3.0')

valor = 0
multiplicar = 0

while True:
    valor = int(input('Quer ver a tabuada de qual valor ? '))
    print('-' * 30)
    if valor < 0:
        break
    for i in range(1, 11):
        multiplicar = valor * i
        print(f'{valor} x {i} = {multiplicar}')
    print('-' * 30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
