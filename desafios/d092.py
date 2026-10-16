
"""
    Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário, se por a caso, a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import date

titulo = "CADASTRO DE TRABALHADOR"
print(f"{"=" * (len(titulo) * 2)}\n{titulo:^46}\n{"=" * (len(titulo) * 2)}")

pessoa_cadastrada = {}
ano_atual = date.today().year

while True:
    while True:
        nome = str(input("Nome: ")).strip().title()
        if nome and all(i.isalpha() or i.isspace() for i in nome):
            pessoa_cadastrada["nome"] = nome
            break
        print("Nome inválido!")

    while True:
        try:
            nascimento = int(input("Ano nascimento: "))
            if nascimento > 1950 and nascimento < ano_atual:
                pessoa_cadastrada["idade"] = ano_atual - nascimento
                break
            elif nascimento > ano_atual:
                print(f"Não tem como você ter nascido depois de {ano_atual}")
            else:
                print("Você não é tão velho assim")
        except ValueError:
            print("Ano de nascimento inválido!")

    while True:
        try:
            ctps = int(input("Carteira de trabalho (0 não tem): "))
            pessoa_cadastrada["ctps"] = ctps
            break
        except ValueError:
            print("CTPS INVÁLIDA!")
    if pessoa_cadastrada["ctps"] == 0:
        break

    while True:
        try:
            ano_contratacao = int(input("Ano de contratação: "))
            if ano_contratacao > pessoa_cadastrada["idade"] and ano_contratacao <= ano_atual:
                pessoa_cadastrada["contratacao"] = ano_contratacao
                break
            else:
                print(f"Digite uma data entre {pessoa_cadastrada["idade"]} e {ano_atual}")
                continue
        except ValueError:
            print("Ano de contratação inválido!")

    while True:
        try:
            salario = float(input("Salário: R$"))
            if salario <= 0:
                continue
            else:
                pessoa_cadastrada["salario"] = salario
                break
        except ValueError:
            print("dado inválido!")

    pessoa_cadastrada["aposentadoria"] = pessoa_cadastrada["idade"] + (pessoa_cadastrada["contratacao"] + 35) - ano_atual

    break

print("=" * (len(titulo) * 2))

for k, v in pessoa_cadastrada.items():
    print(f" - {k} tem o valor {v}")
