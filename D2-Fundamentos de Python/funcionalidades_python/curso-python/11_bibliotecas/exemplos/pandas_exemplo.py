"""
pandas e muito usado para trabalhar com tabelas.
Instale com:
pip install pandas
"""

try:
    import pandas as pd
except ImportError:
    print("Instale a biblioteca com: pip install pandas")
else:
    dados = {
        "produto": ["pao", "queijo", "suco"],
        "quantidade": [10, 5, 8],
    }
    tabela = pd.DataFrame(dados)
    print(tabela)
    print("Total de itens:", tabela["quantidade"].sum())

