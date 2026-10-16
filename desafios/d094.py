
"""
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
    a - quantas pessoas cadastradas;
    b - a média de idade.
    c - uma lista com mulheres;
    d - uma lista com idade acima da média.
"""

titulo = "CADASTRO DE PESSOAS"
print(f"{"=" * (len(titulo) * 2)}\n{titulo:^38}\n{"=" * (len(titulo) * 2)}")

sistema = {}
pessoas = {}
dados_pessoas = []
pessoas_cadastradas = 0
media = 0
mulheres = []

while True:
    while True:
        nome =  str(input("Nome: ").strip().title())
        if nome and all(i.isalpha() or i.isspace() for i in nome):
            pessoas["nome"] = nome
            break
        else:
            print("Nome inválido!")

    while True:        
        sexo = str(input("Sexo [F/M]: ").strip().upper())
        if sexo not in ('F', 'M'):
            print("ERRO! Responda apenas F ou M.")
        else:
            pessoas["sexo"] = sexo
            break
    
    while True:
        try:
            idade = int(input("Idade: "))
            if idade > 0 and idade < 150:
                pessoas["idade"] = idade
                break
            else:
                print("Impossível essa ser a sua idade!")
        except ValueError:
            print("Idade inválida!")
    
    pessoas_cadastradas += 1
    media += pessoas["idade"]
    
    if pessoas["sexo"] == 'F':
        mulheres.append(pessoas["nome"])
    dados_pessoas.append(pessoas.copy())

    while True:
        continuar = str(input("Quer continuar ? [S/N] ").strip().upper())
        if continuar not in ("S", "N"):
            print("ERRO! Responda apennas S ou N.")
        else:
            break
    if continuar == "N":
        break

sistema["dados_pessoas"] = dados_pessoas
media = media // pessoas_cadastradas

print("-=" * len(titulo))
print(f"A) Ao todo temos {pessoas_cadastradas} pessoas cadastradas.")
print(f"B) A média de idade é de {media} anos.")
print(f"C) As mulheres cadastradas foram {", ".join(map(str, mulheres))}.")
print("D) Lista de pessoas que estão com a idade acima da média:")
for i in dados_pessoas:
    if i["idade"] > media:
        print(f"nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]};")
print(f"{"ENCERRADO":=^38}")
