"""
Operadores fazem calculos e comparacoes.
"""

a = 10
b = 3

print("Soma:", a + b)
print("Subtracao:", a - b)
print("Multiplicacao:", a * b)
print("Divisao:", a / b)
print("Divisao inteira:", a // b)
print("Resto da divisao:", a % b)
print("Potencia:", a ** b)

# Operadores compostos mudam a propria variavel.
estoque = 10
print("Estoque inicial:", estoque)

estoque += 5  # igual a: estoque = estoque + 5
print("Depois de comprar mais 5:", estoque)

estoque -= 2
print("Depois de vender 2:", estoque)

estoque *= 3
print("Depois de triplicar o estoque:", estoque)

