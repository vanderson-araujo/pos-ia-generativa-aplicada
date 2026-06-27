"""
Python permite retornar mais de um valor.
Na pratica, ele devolve uma tupla.
"""


def calcular_pedido(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.10
    total = subtotal - desconto
    return subtotal, desconto, total


subtotal, desconto, total = calcular_pedido(20, 3)

print("Subtotal:", subtotal)
print("Desconto:", desconto)
print("Total:", total)

