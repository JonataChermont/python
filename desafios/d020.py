


import random

alunos = []
alunos.insert(0, input("digite o nome do primeiro aluno: "))
alunos.insert(1, input("digite o nome do segundo aluno: "))
alunos.insert(2, input("digite o nome do terceiro aluno: "))
alunos.insert(3, input("digite o nome do quarto aluno: "))

embaralhar = random.shuffle(alunos)

print(f"A ordem de apresentação será {alunos}")

