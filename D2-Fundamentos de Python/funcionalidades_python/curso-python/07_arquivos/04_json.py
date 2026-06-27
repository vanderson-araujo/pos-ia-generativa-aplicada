"""
JSON e muito usado para configuracoes e APIs.
"""

import json

produto = {
    "nome": "X-Burguer",
    "preco": 18.90,
    "disponivel": True,
}

with open("produto.json", "w", encoding="utf-8") as arquivo:
    json.dump(produto, arquivo, indent=4, ensure_ascii=False)

with open("produto.json", "r", encoding="utf-8") as arquivo:
    produto_lido = json.load(arquivo)

print("Produto:", produto_lido["nome"])
print("Preco:", produto_lido["preco"])

