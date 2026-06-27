"""
Organiza arquivos de exemplo por extensao.
O script cria uma pasta temporaria chamada arquivos_exemplo.
"""

from pathlib import Path
import shutil

pasta = Path("arquivos_exemplo")
pasta.mkdir(exist_ok=True)

for nome in ["relatorio.txt", "foto.jpg", "planilha.csv"]:
    (pasta / nome).write_text("arquivo de estudo", encoding="utf-8")

for arquivo in pasta.iterdir():
    if arquivo.is_file():
        extensao = arquivo.suffix.replace(".", "") or "sem_extensao"
        destino = pasta / extensao
        destino.mkdir(exist_ok=True)
        shutil.move(str(arquivo), destino / arquivo.name)

print("Arquivos organizados dentro de arquivos_exemplo.")

