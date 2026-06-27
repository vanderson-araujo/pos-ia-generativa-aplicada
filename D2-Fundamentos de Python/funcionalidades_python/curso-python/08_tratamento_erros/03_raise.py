"""
raise permite gerar um erro de proposito.
Isso e util para impedir valores invalidos.
"""


def sacar(saldo: float, valor: float) -> float:
    if valor <= 0:
        raise ValueError("O valor do saque precisa ser positivo.")
    if valor > saldo:
        raise ValueError("Saldo insuficiente.")
    return saldo - valor


try:
    novo_saldo = sacar(100, 30)
    print("Novo saldo:", novo_saldo)
except ValueError as erro:
    print("Erro:", erro)

