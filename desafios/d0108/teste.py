
"""
    ENUNCIADO DESAFIO 108
    Adapte o código do DESAFIO 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
"""

"""
    ENUNCIADO DESAFIO 107
    Crie um programa chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

import moeda

price = float(input("Digite o preço: R$"))

print(f"A metade de {moeda.coin(price)} é {moeda.coin(moeda.half(price))}")
print(f"O dobro de {moeda.coin(price)} é {moeda.coin(moeda.double(price))}")
print(f"Aumentando 10%, temos {moeda.coin(moeda.increase(price, 10))}")
