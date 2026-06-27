"""
Percorrer colecoes permite processar item por item.
"""

estoque = {
    "pao": 20,
    "queijo": 15,
    "hamburguer": 10,
}

for produto, quantidade in estoque.items():
    print(f"{produto}: {quantidade} unidades")

nomes = ["Ana", "Bruno", "Carla"]

for posicao, nome in enumerate(nomes, start=1):
    print(f"{posicao}. {nome}")

