"""
Exemplo didatico de preparacao para imprimir um documento.
No Windows, os.startfile(arquivo, "print") pode enviar para impressora padrao.
Por seguranca, este exemplo apenas mostra o caminho.
"""

from pathlib import Path

arquivo = Path("documento_para_imprimir.txt")
arquivo.write_text("Documento de teste para impressao.\n", encoding="utf-8")

print("Documento criado:", arquivo.resolve())
print("Confira o arquivo antes de imprimir.")

# No Windows, depois de conferir, voce poderia usar:
# import os
# os.startfile(arquivo, "print")

