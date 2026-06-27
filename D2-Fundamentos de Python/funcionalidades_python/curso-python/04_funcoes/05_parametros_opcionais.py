"""
Parametros opcionais possuem valor padrao.
Se a pessoa nao informar, Python usa o padrao.
"""


def montar_lanche(nome, queijo=True):
    if queijo:
        print(f"{nome} com queijo")
    else:
        print(f"{nome} sem queijo")


montar_lanche("X-burguer")
montar_lanche("X-salada", queijo=False)

