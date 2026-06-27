"""
Literal indica valores aceitos especificos.
E util para documentar opcoes limitadas.
"""

from typing import Literal

Tamanho = Literal["P", "M", "G"]


def calcular_frete(tamanho: Tamanho) -> float:
    if tamanho == "P":
        return 10.0
    if tamanho == "M":
        return 15.0
    return 20.0


print("Frete tamanho M:", calcular_frete("M"))

