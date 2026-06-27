"""
requests facilita consumir APIs HTTP.
Instale com:
pip install requests
"""

try:
    import requests
except ImportError:
    print("Instale a biblioteca com: pip install requests")
else:
    resposta = requests.get("https://api.github.com", timeout=10)
    print("Status:", resposta.status_code)
    print("Tipo de conteudo:", resposta.headers.get("content-type"))

