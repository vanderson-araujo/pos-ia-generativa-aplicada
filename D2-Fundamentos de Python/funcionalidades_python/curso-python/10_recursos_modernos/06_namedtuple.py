"""
namedtuple cria uma tupla com nomes para os campos.
Hoje, muitas vezes dataclass e mais flexivel, mas namedtuple ainda aparece.
"""

from collections import namedtuple

Endereco = namedtuple("Endereco", ["rua", "numero", "cidade"])

endereco = Endereco("Rua das Flores", 100, "Campinas")

print("Rua:", endereco.rua)
print("Cidade:", endereco.cidade)

