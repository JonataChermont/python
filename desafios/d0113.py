
"""
    Reescreva função leia_int() que fizemos no desafio 104, incluindo agora a possibilidade de digitação de um número de tipo inválido. Aproveite e crie também a função leia_float() com a mesma funcionalidade,
"""

from funcoes_globais import titulo

titulo("FUNÇÕES APROFUNDADAS EM PYTHON")

def leia_int(msg="Digite um número inteiro: "):
    while True:
        try:
            number = int(input(msg))
        except:  # noqa: E722
            print("\033[1;31mERRO: por favor, digite um número inteiro válido! Exemplo: 10.\033[0m")
        else:
            return number

def leia_float(msg="Digite um número real: "):
    while True:
        try:
            number = float(input(msg))
        except:  # noqa: E722
            print("\033[1;31mERRO: por favor, digite um número real válido! Exemplo: 2.5\033[m")
        else:
            return number

numero_inteiro = leia_int()
numero_real = leia_float()
print(f"O valor inteiro digitado foi o {numero_inteiro} e o real foi {numero_real}")