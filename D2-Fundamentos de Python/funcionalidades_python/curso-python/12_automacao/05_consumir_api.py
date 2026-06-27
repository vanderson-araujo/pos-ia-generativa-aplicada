"""
Consumindo uma API usando apenas biblioteca padrao do Python.
"""

import json
from urllib.request import urlopen

url = "https://api.github.com"

try:
    with urlopen(url, timeout=10) as resposta:
        dados = json.loads(resposta.read().decode("utf-8"))
except Exception as erro:
    print("Nao foi possivel acessar a API:", erro)
else:
    print("API acessada com sucesso.")
    print("URL de eventos:", dados.get("events_url"))

