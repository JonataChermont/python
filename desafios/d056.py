
"""
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
    No final do programa, mostre:
    - a média de idade do grupo;
    - qual é o nome do homem mais velho;
    - quantas mulheres tem menos de 20 anos
"""
print('ANALISADOR COMPLETO')
media = 0
mais_velho = 0
nome_mais_velho = ''
mulheres = 0
mulher_menos_vinte_anos = 0
for i in range(1, 5):
    print(f' {i}ª PESSOA '.center(20, '-'))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('[M/F]: ').strip().upper()
    media += idade / 4
    if 'M' in sexo:
        if i == 1:
            mais_velho = idade
        else:
            if idade > mais_velho:
                mais_velho = idade
                nome_mais_velho = nome
    if 'F' in sexo:
        mulheres += 1
        if idade < 20:
            mulher_menos_vinte_anos += 1

print(f'A média de idade do grupo é de {media:.2f} anos')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_mais_velho}')
print(f'Ao todo são {mulher_menos_vinte_anos} mulheres com menos de 20 anos')