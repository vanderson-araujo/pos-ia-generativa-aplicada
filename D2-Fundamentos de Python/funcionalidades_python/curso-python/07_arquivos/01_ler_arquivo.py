"""
Lendo um arquivo de texto.
Se o arquivo nao existir, criamos um exemplo antes de ler.
"""

from pathlib import Path

arquivo = Path("recado.txt")

if not arquivo.exists():
    arquivo.write_text("Estudar Python um pouco por dia ajuda muito.\n", encoding="utf-8")

conteudo = arquivo.read_text(encoding="utf-8")
print("Conteudo do arquivo:")
print(conteudo)

