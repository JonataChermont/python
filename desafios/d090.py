
"""
    Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

titulo = "DICIONARIO EM PYTHON"
print(f"{"=" * (len(titulo) * 2)}\n{titulo:^40}\n{"=" * (len(titulo) * 2)}")

aluno = {}

while True:
    nome = str(input('Nome: ')).strip().title()
    if nome and all(i.isalpha() or i.isspace() for i in nome):
        break
    print('Nome inválido!')
    
while True:
    try:
        media = float(input(f'Média de {nome}: '))
        if media >= 0 and media <= 10:
            break
    except ValueError:
        print('Média inválida!')

aluno["nome"] = nome
aluno["media"] = media

print("-=" * len(titulo))

print(f" - nome é igual a {aluno['nome']}")
print(f" - média é igual a {aluno['media']}")
print(" - situação é igual a", end=' ')
if aluno["media"] < 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")

