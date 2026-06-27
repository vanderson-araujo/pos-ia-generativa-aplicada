"""
Hamburgueria Divertida

Cada lanche fica em um arquivo diferente dentro da pasta lanches.
Este exemplo mostra como separar responsabilidades usando modulos.
"""

from chapa import preparar_na_chapa
from ingredientes import mostrar_ingredientes
from lanches import x_bacon, x_burguer, x_salada

lanches = [
    x_burguer.criar_lanche(),
    x_salada.criar_lanche(),
    x_bacon.criar_lanche(),
]

print("Cardapio da Hamburgueria Divertida")

for lanche in lanches:
    print(lanche.resumo())

escolhido = lanches[1]
preparar_na_chapa(escolhido.nome)
mostrar_ingredientes(escolhido.nome, escolhido.ingredientes)

