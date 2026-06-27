"""
Operador ternario permite escolher um valor em uma unica linha.
Use com moderacao: se ficar dificil de ler, prefira if/else normal.
"""

idade = 20

mensagem = "maior de idade" if idade >= 18 else "menor de idade"
print("Situacao:", mensagem)

estoque = 0
status = "disponivel" if estoque > 0 else "esgotado"
print("Produto:", status)

