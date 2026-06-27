"""
Polimorfismo permite usar objetos diferentes por uma interface parecida.
"""


class Boleto:
    def pagar(self) -> None:
        print("Pagamento via boleto.")


class Pix:
    def pagar(self) -> None:
        print("Pagamento via Pix.")


formas_pagamento = [Boleto(), Pix()]

for forma in formas_pagamento:
    forma.pagar()

