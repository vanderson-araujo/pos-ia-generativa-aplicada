"""
Consultando dados com SELECT.
"""

import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("SELECT id, nome, preco FROM produtos")
produtos = cursor.fetchall()

for produto in produtos:
    print(f"ID {produto[0]} - {produto[1]} - R$ {produto[2]:.2f}")

conexao.close()

