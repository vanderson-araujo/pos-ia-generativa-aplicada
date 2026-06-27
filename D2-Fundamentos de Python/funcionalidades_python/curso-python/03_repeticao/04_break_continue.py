"""
break encerra o loop.
continue pula para a proxima repeticao.
"""

produtos = ["pao", "leite", "cafe", "bolo"]

for produto in produtos:
    if produto == "cafe":
        print("Cafe encontrado. Parando busca.")
        break
    print("Verificando:", produto)

print("Mostrando produtos, exceto leite:")
for produto in produtos:
    if produto == "leite":
        continue
    print(produto)

