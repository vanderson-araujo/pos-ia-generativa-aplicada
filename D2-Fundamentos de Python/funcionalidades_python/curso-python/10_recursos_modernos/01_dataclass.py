"""
dataclass cria automaticamente partes repetitivas de uma classe.
Ela lembra um record em Java, quando queremos representar dados.
"""

from dataclasses import dataclass


@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int


produto = Produto("Mouse", 89.90, 12)
print(produto)
print("Nome:", produto.nome)

