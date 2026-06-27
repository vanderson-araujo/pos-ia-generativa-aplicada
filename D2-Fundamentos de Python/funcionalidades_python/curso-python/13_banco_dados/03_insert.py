"""
Inserindo dados na tabela.
"""

import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute(
    "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
    ("X-Burguer", 18.90),
)

conexao.commit()
conexao.close()

print("Produto inserido.")

