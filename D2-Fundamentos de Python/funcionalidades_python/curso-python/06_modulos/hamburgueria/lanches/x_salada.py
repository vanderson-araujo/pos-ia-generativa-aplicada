from lanche import Lanche


def criar_lanche() -> Lanche:
    return Lanche(
        nome="X-Salada",
        ingredientes=["pao", "hamburguer", "queijo", "alface", "tomate"],
        preco=21.90,
    )

