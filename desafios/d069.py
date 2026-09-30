
"""
    Crie um programa que leia a idade e o sexo de várias pessoas.
    A cada pessoa cadastrada, o programa deverá perguntar se o usuário
    quer ou não continuar. No final, mostre:
    - quantas pessoas tem mais de 18 anos;
    - quantos homens foram cadastrados;
    - quantas mulheres tem menos de 20 anos.
"""

titulo = 'CADASTRE UMA PESSOA'
print(f'{'=' * len(titulo)}\n{titulo}\n{'=' * len(titulo)}')

maioridade = 0
homens = 0
mulheres_menos_vinte_anos = 0

while True:
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        maioridade += 1
    if 'M' in sexo:
        homens += 1
    if 'F' in sexo and idade < 20:
        mulheres_menos_vinte_anos += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_menos_vinte_anos} mulheres com menos de 20 anos')
