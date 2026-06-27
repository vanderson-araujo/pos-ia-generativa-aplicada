"""
Arquivo principal.
Ele importa funcoes de outros arquivos da mesma pasta.
"""

import calculadora
from mensagens import boas_vindas, despedida

boas_vindas()

print("Soma:", calculadora.somar(10, 5))
print("Subtracao:", calculadora.subtrair(10, 5))
print("Multiplicacao:", calculadora.multiplicar(10, 5))
print("Divisao:", calculadora.dividir(10, 5))

despedida()

