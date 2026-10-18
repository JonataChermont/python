
"""
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

from datetime import date

from funcoes_globais import titulo

titulo("FUNÇÕES PARA VOTAÇÃO", "=")


ano_atual = date.today().year

def voto(ano):
    idade = ano_atual - ano
    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO."
    elif idade >= 16 and idade < 18 or idade >= 70:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else: 
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."

while True:
    ano_nascimento = int(input("Em que ano você nasceu: "))
    if ano_nascimento < ano_atual:
        break

print(voto(ano_nascimento))
