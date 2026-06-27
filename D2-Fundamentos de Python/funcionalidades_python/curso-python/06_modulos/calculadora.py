"""
Modulo com funcoes de calculadora.
Este arquivo sera importado por main.py.
"""


def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Nao e possivel dividir por zero.")
    return a / b

