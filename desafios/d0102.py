
"""
    Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

from funcoes_globais import titulo

titulo("FUNÇÃO PARA FATORIAL", "=")

def fatorial(num, show=False):
    """
        -> Calcula o fatorial de um número.
        :param num: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número num.
    """
    fat = 1
    print(f"{num}! = ", end="")
    while num > 0:
        if show == True:
            print(num, end="")
            if num > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
                return fat
        fat *= num
        num -= 1
    return fat

print(fatorial(10, False))
