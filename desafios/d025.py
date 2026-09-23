
#crie um programa que leia o nome de uma pessoa e diga
#se ela tem "silva" no nome
print('PROCURANDO UMA STRING DENTRO DE OUTRA')

nome = input('Qual seu nome completo ? ').strip().lower()
print(f'Seu nome tem Silva ? {'silva' in nome}')
