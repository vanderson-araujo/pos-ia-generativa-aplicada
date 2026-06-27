"""
Deletando um produto.
"""

import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("DELETE FROM produtos WHERE nome = ?", ("X-Burguer",))

conexao.commit()
conexao.close()

print("Produto removido.")

