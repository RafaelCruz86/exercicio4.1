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

@app.get("/health", operation_id="health")
def health():
    return {"status": "ok"}

@app.post("/tarefas", status_code=201, operation_id="post_tarefa")
def post_tarefa(tarefa: TarefaIn):
    global _proximo_id
    nova = {"id": _proximo_id, "titulo": tarefa.titulo, "concluida": False}
    _tarefas[_proximo_id] = nova
    _proximo_id += 1
    return nova

@app.get("/tarefas/{id}", operation_id="get_tarefa")
def get_tarefa(id: int):
    if id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return _tarefas[id]

@app.get("/tarefas")
def listar_tarefas():
    return list(_tarefas.values())

@app.put("/tarefas/{id}", operation_id="put_tarefa")
def put_tarefa(id: int, tarefa: TarefaUpdate):
    if id not in _tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa_atualizada = {"id": id, "titulo": tarefa.titulo, "concluida": tarefa.concluida}
    _tarefas[id] = tarefa_atualizada
    return tarefa_atualizada