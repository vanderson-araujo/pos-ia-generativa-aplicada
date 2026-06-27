"""
Funcoes para listar ingredientes.
"""


def mostrar_ingredientes(nome: str, ingredientes: list[str]) -> None:
    print(f"\n{name_for_print(nome)}")
    print("-" * 30)
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")


def name_for_print(nome: str) -> str:
    return nome.upper()

