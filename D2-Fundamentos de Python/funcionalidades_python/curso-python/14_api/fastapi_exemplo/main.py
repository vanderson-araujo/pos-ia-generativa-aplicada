"""
Primeira API com FastAPI.

Para executar:
uvicorn main:app --reload
"""

from fastapi import FastAPI, HTTPException

app = FastAPI(title="API da Hamburgueria")

lanches = {
    1: {"nome": "X-Burguer", "preco": 18.90},
    2: {"nome": "X-Salada", "preco": 21.90},
    3: {"nome": "X-Bacon", "preco": 24.90},
}


@app.get("/")
def inicio() -> dict[str, str]:
    return {"mensagem": "Bem-vindo a API da Hamburgueria"}


@app.get("/lanches")
def listar_lanches() -> dict[int, dict[str, float | str]]:
    return lanches


@app.get("/lanches/{lanche_id}")
def buscar_lanche(lanche_id: int) -> dict[str, float | str]:
    if lanche_id not in lanches:
        raise HTTPException(status_code=404, detail="Lanche nao encontrado")
    return lanches[lanche_id]

