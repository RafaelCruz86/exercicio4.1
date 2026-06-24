from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Store em memória. Zera quando o processo reinicia.
_tarefas: dict[int, dict] = {}
_proximo_id = 1

class TarefaIn(BaseModel):
    titulo: str

class TarefaUpdate(BaseModel):
    titulo: str
    concluida: bool

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tarefas", status_code=201)
def criar(tarefa: TarefaIn):
    global _proximo_id
    nova = {"id": _proximo_id, "titulo": tarefa.titulo, "concluida": False}
    _tarefas[_proximo_id] = nova
    _proximo_id += 1
    return nova

# --- Novos Endpoints Implementados Abaixo ---

@app.get("/tarefas/{id}")
def obter_por_id(id: int):
    if id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return _tarefas[id]

@app.get("/tarefas")
def listar_todas():
    # Retorna uma lista contendo todas as tarefas armazenadas no dicionário
    return list(_tarefas.values())

@app.put("/tarefas/{id}")
def atualizar(id: int, tarefa: TarefaUpdate):
    if id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    # Atualiza os dados mantendo o mesmo ID
    tarefa_atualizada = {
        "id": id,
        "titulo": tarefa.titulo,
        "concluida": tarefa.concluida
    }
    _tarefas[id] = tarefa_atualizada
    return tarefa_atualizada