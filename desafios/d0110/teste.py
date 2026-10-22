
"""
    Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que ja temos no módulo criado até aqui.
"""

import moeda

price = float(input("Digite o preço: R$"))
moeda.summary(price, 20, 12) #10 = aumento; 12 = redução
