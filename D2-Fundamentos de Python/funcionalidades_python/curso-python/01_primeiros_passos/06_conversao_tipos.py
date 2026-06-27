"""
Converter tipos e necessario quando queremos transformar texto em numero,
numero em texto, e assim por diante.
"""

idade_texto = "30"
idade_numero = int(idade_texto)

print("Daqui a 5 anos voce tera:", idade_numero + 5)

preco_texto = "19.90"
preco = float(preco_texto)
print("Preco com desconto:", preco - 2)

numero = 42
mensagem = "O numero escolhido foi " + str(numero)
print(mensagem)

# Cuidado: int("abc") gera erro, porque "abc" nao e um numero.

