"""
Anotacoes de tipo documentam o que a funcao espera e retorna.
Python nao impede automaticamente outro tipo em tempo de execucao.
"""


def calcular_total(precos: list[float]) -> float:
    return sum(precos)


valores = [10.0, 20.5, 7.25]
print("Total:", calcular_total(valores))

