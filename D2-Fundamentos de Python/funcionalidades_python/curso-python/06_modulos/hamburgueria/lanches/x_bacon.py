from lanche import Lanche


def criar_lanche() -> Lanche:
    return Lanche(
        nome="X-Bacon",
        ingredientes=["pao", "hamburguer", "queijo", "bacon crocante"],
        preco=24.90,
    )

