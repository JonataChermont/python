
"""
    Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
    - quantidade de notas;
    - a maior nota;
    - a menor nota;
    - a média da turma;
    - a situação (opcional);
    - adicionar as docstrings.
"""

from funcoes_globais import titulo

titulo("ANALISANDO E GERENDO DICIONARIOS", "=")

student = {}

def student_grades(*notes, situation=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param notes: uma ou mais notas dos alunos (aceita várias)
        :param situation: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma.
    """
    total = len(notes)
    average = 0
    for i in notes:
        average += i
    average = average / total
    status = ""
    if average < 5:
        status = "RUIM"
    elif average >= 5 and average < 7:
        status = "RAZOÁVEL"
    else:
        status = "BOA"

    student["total"] = total
    student["maior"] = max(notes)
    student["menor"] = min(notes)
    student["media"] = average
    if situation:
        student["situacao"] = status
    return student

# PROGRAMA PRINCIPAL
response  = student_grades(1, 3, 5, 2, 10, situation=True)
print(response)