"""
Escrevendo em um arquivo de texto.
O modo "w" substitui o conteudo anterior.
"""

with open("lista_compras.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("arroz\n")
    arquivo.write("feijao\n")
    arquivo.write("cafe\n")

print("Arquivo lista_compras.txt criado.")

