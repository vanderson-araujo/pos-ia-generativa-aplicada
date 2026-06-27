"""
dict guarda pares chave/valor.
Ele lembra um Map em Java.
"""

pessoa = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "Sao Paulo",
}

print("Nome:", pessoa["nome"])
print("Pessoa completa:", pessoa)

pessoa["email"] = "ana@email.com"
print("Com email:", pessoa)

