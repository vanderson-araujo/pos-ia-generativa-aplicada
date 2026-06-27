from lanche import Lanche


def criar_lanche() -> Lanche:
    return Lanche(
        nome="X-Burguer",
        ingredientes=["pao", "hamburguer", "queijo"],
        preco=18.90,
    )

