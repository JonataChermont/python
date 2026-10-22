
"""
    Crie um pacote chamado utilidadescev que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utlizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.
"""

from utilidadescev import moeda

price = float(input("Digite o preço: R$"))
moeda.summary(price, 20, 12) #10 = aumento; 12 = redução
