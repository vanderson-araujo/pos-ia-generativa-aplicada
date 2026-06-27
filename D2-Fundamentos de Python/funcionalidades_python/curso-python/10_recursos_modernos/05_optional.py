"""
Optional indica que um valor pode existir ou ser None.
No Python 3.11 tambem podemos escrever str | None.
"""


def buscar_email(nome: str) -> str | None:
    contatos = {"Ana": "ana@email.com", "Bruno": "bruno@email.com"}
    return contatos.get(nome)


email = buscar_email("Carla")

if email is None:
    print("Email nao encontrado.")
else:
    print("Email:", email)

