# FastAPI Exemplo

## Objetivo

Mostrar uma API pequena para cadastro de lanches em memoria.

## Como executar

Na pasta `14_api`, instale:

```bash
pip install -r requirements.txt
```

Depois, dentro de `14_api/fastapi_exemplo`, rode:

```bash
python -m uvicorn main:app --reload
```

## Rotas
Para testar as rotas uma opção é utilizar o Postman
- `GET /`: mensagem inicial
- `GET /lanches`: lista lanches cadastrados
- `GET /lanches/{lanche_id}`: busca um lanche por id

