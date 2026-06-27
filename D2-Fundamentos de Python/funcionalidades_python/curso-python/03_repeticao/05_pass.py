"""
pass e usado quando o bloco precisa existir, mas ainda nao tem codigo.
Ele evita erro de sintaxe.
"""

opcao = "relatorio"

if opcao == "relatorio":
    pass  # Futuramente vamos gerar um relatorio aqui.
else:
    print("Opcao nao implementada.")

print("Programa continuou normalmente.")

