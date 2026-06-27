"""
CSV e um formato muito usado em planilhas.
Aqui criamos e depois lemos um arquivo CSV simples.
"""

import csv

with open("pessoas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["nome", "idade"])
    escritor.writerow(["Ana", 28])
    escritor.writerow(["Bruno", 35])

with open("pessoas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"{linha['nome']} tem {linha['idade']} anos.")

