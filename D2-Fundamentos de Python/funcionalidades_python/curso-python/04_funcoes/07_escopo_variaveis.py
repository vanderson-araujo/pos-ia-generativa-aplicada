"""
Escopo e onde uma variavel existe.
Variaveis criadas dentro de uma funcao sao variaveis locais.
"""

mensagem_global = "Sou visivel no arquivo todo."


def exemplo_escopo():
    mensagem_local = "Sou visivel apenas dentro da funcao."
    print(mensagem_local)
    print(mensagem_global)


exemplo_escopo()

# A linha abaixo daria erro, porque mensagem_local nao existe aqui fora.
# print(mensagem_local)

