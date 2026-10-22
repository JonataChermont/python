
"""
    Dentro do pacote utilidadescev que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada LeiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""

from utilidadescev import moeda  # noqa: I001

from utilidadescev import dado

price = dado.read_money("Digite o preço: R$")
moeda.summary(price, 35, 22)
