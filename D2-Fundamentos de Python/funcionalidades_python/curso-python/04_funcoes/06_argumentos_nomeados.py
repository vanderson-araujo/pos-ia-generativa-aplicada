"""
Argumentos nomeados deixam a chamada da funcao mais clara.
"""


def cadastrar_pessoa(nome, idade, cidade):
    print(f"{nome}, {idade} anos, mora em {cidade}.")


cadastrar_pessoa(nome="Carla", idade=31, cidade="Curitiba")
cadastrar_pessoa(cidade="Recife", nome="Diego", idade=27)

