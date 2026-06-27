"""
Atributos guardam dados.
Metodos sao funcoes dentro da classe.
"""


class Produto:
    nome = "Caderno"
    preco = 15.90

    def mostrar(self):
        print(f"{self.nome} custa R$ {self.preco:.2f}")


produto = Produto()
produto.mostrar()

