
#faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente
print('PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA')

nome = input('Digite seu nome completo: ').strip().title()
print('Muito prazer em te conhecer!')

print(f'Seu primeiro nome é {nome.split()[0]}')
print(f'Seu último nome é {nome.split()[len(nome.split()) - 1]}')
