"""
Classe simples para representar um lanche.
"""


class Lanche:
    def __init__(self, nome: str, ingredientes: list[str], preco: float):
        self.nome = nome
        self.ingredientes = ingredientes
        self.preco = preco

    def resumo(self) -> str:
        return f"{self.nome} - R$ {self.preco:.2f}"

