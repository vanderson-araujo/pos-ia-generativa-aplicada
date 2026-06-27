"""
Operadores logicos combinam condicoes.
and: todas as condicoes precisam ser verdadeiras.
or: pelo menos uma condicao precisa ser verdadeira.
not: inverte verdadeiro/falso.
"""

tem_cadastro = True
saldo = 35
valor_compra = 30

if tem_cadastro and saldo >= valor_compra:
    print("Compra aprovada.")
else:
    print("Compra recusada.")

cupom = "PYTHON10"

if cupom == "PYTHON10" or cupom == "ESTUDO10":
    print("Cupom valido.")

if not saldo < 0:
    print("Saldo nao esta negativo.")

