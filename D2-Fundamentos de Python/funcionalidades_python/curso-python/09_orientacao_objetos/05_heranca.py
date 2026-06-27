"""
Heranca permite criar uma classe baseada em outra.
"""


class Funcionario:
    def __init__(self, nome: str):
        self.nome = nome

    def bater_ponto(self) -> None:
        print(f"{self.nome} bateu ponto.")


class Gerente(Funcionario):
    def aprovar_ferias(self) -> None:
        print(f"{self.nome} aprovou ferias.")


gerente = Gerente("Patricia")
gerente.bater_ponto()
gerente.aprovar_ferias()

