
"""
    Crie um programa que leia vários números inteiros pelo teclado.
    O programa só vai parar quando o usuário digitar o valor 999, que
    é a condição de parada. No final, mostre quantos números foram digitados
    e qual foi a soma entre eles (desconsiderando o flag).
"""
print('TRATANDO VÁRIOS VALORES')

numero = int(input('Digite um número inteiro [999 para parar]: '))
contador = 0
soma = numero

while numero != 999:
    numero = int(input('Digite um número inteiro [999 para parar]: '))
    contador += 1
    soma += numero

print(f'Voçê digitou {contador} números e a soma entre eles foi {soma - 999}')
