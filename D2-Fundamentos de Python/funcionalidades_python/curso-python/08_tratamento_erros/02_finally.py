"""
finally executa sempre, dando erro ou nao.
Ele e util para fechar recursos, como arquivos e conexoes.
"""

try:
    print("Tentando abrir um arquivo.")
    arquivo = open("arquivo_que_nao_existe.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Arquivo nao encontrado.")
finally:
    print("Fim da tentativa.")

