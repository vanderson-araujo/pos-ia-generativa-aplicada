"""
set guarda valores unicos, sem repeticao.
"""

categorias = {"lanche", "bebida", "lanche", "sobremesa"}

print(categorias)
print("Quantidade de categorias:", len(categorias))

categorias.add("combo")
print("Depois do add:", categorias)

