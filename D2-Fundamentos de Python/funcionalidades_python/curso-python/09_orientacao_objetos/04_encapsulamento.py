"""
Encapsulamento protege detalhes internos.
Em Python, um atributo com _ indica que ele deve ser tratado como interno.
"""


class Conta:
    def __init__(self, saldo_inicial: float):
        self._saldo = saldo_inicial

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self._saldo += valor

    def mostrar_saldo(self) -> None:
        print(f"Saldo: R$ {self._saldo:.2f}")


conta = Conta(100)
conta.depositar(50)
conta.mostrar_saldo()

