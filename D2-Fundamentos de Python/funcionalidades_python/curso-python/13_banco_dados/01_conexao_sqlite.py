"""
Criando uma conexao com SQLite.
sqlite3 ja vem com Python.
"""

import sqlite3

conexao = sqlite3.connect("loja.db")
print("Conexao criada com sucesso.")
conexao.close()

