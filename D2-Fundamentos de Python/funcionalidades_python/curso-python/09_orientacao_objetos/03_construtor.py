"""
__init__ e o construtor.
Ele roda quando criamos um objeto.
"""


class Cliente:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def apresentar(self) -> None:
        print(f"{self.nome} - {self.email}")


cliente = Cliente("Marina", "marina@email.com")
cliente.apresentar()

