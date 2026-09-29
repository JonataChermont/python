
"""
    Crie um programa que leia vários números inteiros pelo teclado.
    No final da execução, mostre a média entre todos os valores e
    qual foi o maior e o menor valores lidos. O programa deve perguntar
    ao usuário se ele quer ou não continuar a digitar valores
"""
print('MAIOR E MENOR VALORES')

numero = int(input('Digite um número: '))
continuar = str(input('Quer continuar ? [S/N]')).strip().upper()
contador = 1
media = numero
maior = numero
menor = numero

while continuar != 'N':
    numero = int(input('Digite um número: '))
    continuar = str(input('Quer continuar ? [S/N]')).strip().upper()
    contador += 1
    media += numero
    if maior < numero:
        maior = numero
    if menor > numero:
        menor = numero

print(f'Voçê digitou {contador} números e a média foi {media / contador:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
