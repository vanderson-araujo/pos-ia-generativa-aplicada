"""
Tipos basicos sao categorias de valores.
Python entende automaticamente o tipo a partir do valor informado.
"""

texto = "lista de compras"
quantidade = 3
preco = 12.50
ativo = True

print(texto, "->", type(texto))
print(quantidade, "->", type(quantidade))
print(preco, "->", type(preco))
print(ativo, "->", type(ativo))

# Podemos juntar textos com f-string, uma forma pratica de montar mensagens.
print(f"Vou comprar {quantidade} itens. Total aproximado: R$ {preco:.2f}")

