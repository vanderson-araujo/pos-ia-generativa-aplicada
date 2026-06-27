"""
try tenta executar um bloco.
except captura um erro especifico.
"""

texto = "abc"

try:
    numero = int(texto)
    print(numero)
except ValueError:
    print("Nao foi possivel converter o texto para numero.")

