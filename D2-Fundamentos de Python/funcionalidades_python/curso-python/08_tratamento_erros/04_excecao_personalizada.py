"""
Podemos criar nossos proprios tipos de erro.
"""


class ProdutoEsgotadoError(Exception):
    pass


def vender(produto: str, estoque: int) -> None:
    if estoque <= 0:
        raise ProdutoEsgotadoError(f"{produto} esta esgotado.")
    print(f"Venda realizada: {produto}")


try:
    vender("X-Bacon", 0)
except ProdutoEsgotadoError as erro:
    print("Nao foi possivel vender:", erro)

