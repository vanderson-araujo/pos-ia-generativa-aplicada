"""
Atualizando um produto.
"""

import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute(
    "UPDATE produtos SET preco = ? WHERE nome = ?",
    (19.90, "X-Burguer"),
)

conexao.commit()
conexao.close()

print("Produto atualizado.")

