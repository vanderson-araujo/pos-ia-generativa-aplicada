"""
list guarda varios valores e permite alteracoes.
Ela lembra um ArrayList em Java.
"""

compras = ["arroz", "feijao", "leite"]
print("Lista inicial:", compras)

compras.append("cafe")
print("Depois do append:", compras)

compras.remove("feijao")
print("Depois do remove:", compras)

print("Primeiro item:", compras[0])

