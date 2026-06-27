"""
Enum representa um conjunto fixo de opcoes.
"""

from enum import Enum


class StatusPedido(Enum):
    RECEBIDO = "recebido"
    PREPARANDO = "preparando"
    ENTREGUE = "entregue"


status = StatusPedido.PREPARANDO
print("Status:", status.value)

