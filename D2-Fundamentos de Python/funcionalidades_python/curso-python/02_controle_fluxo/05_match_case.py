"""
match case compara um valor com varios padroes.
Ele lembra o switch de algumas linguagens, como Java moderno.
"""

opcao = "lanche"

match opcao:
    case "lanche":
        print("Voce escolheu um x-burguer.")
    case "bebida":
        print("Voce escolheu um suco.")
    case "sobremesa":
        print("Voce escolheu um brownie.")
    case _:
        print("Opcao desconhecida.")

