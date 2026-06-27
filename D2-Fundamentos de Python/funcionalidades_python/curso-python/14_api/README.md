# 14 - API

## Objetivo

Criar uma primeira API com FastAPI.

## Conceitos abordados

- instalacao do FastAPI
- criacao de rotas
- retorno em JSON
- servidor local com Uvicorn

## Como executar

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Entre na pasta do exemplo:

```bash
cd fastapi_exemplo
uvicorn main:app --reload
```

Abra no navegador:

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

## Observacoes

FastAPI e uma biblioteca externa. O endpoint `/docs` mostra uma documentacao
interativa criada automaticamente.

