# Exercício 4.1 – API REST de Tarefas

API REST construída com FastAPI para gerenciamento de tarefas (to-do list), desenvolvida como exercício do curso IDP Governo Digital.

## Como executar

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

A API ficará disponível em `http://localhost:8000`.

## Endpoints

| Método | Rota            | Descrição                    |
|--------|-----------------|------------------------------|
| GET    | `/health`       | Verifica se a API está ativa |
| POST   | `/tarefas`      | Cria uma nova tarefa         |
| GET    | `/tarefas`      | Lista todas as tarefas       |
| GET    | `/tarefas/{id}` | Retorna uma tarefa pelo ID   |
| PUT    | `/tarefas/{id}` | Atualiza uma tarefa pelo ID  |

## Modelo de dados

```json
{ "id": 1, "titulo": "estudar APIs", "concluida": false }
```
