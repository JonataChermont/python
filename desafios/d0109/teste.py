
"""
    Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no DESAFIO 108.
"""

import moeda

price = float(input("Digite o preço: R$"))

print(f"A metade de {moeda.coin(price)} é {moeda.half(price)}")
print(f"O dobro de {moeda.coin(price)} é {moeda.double(price)}")
print(f"Aumentando 10%, temos {moeda.increase(price, 10)}")
