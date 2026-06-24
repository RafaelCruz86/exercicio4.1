from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tarefas: dict = {}
contador: int = 0


class TarefaCreate(BaseModel):
    titulo: str


class TarefaUpdate(BaseModel):
    titulo: str
    concluida: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: TarefaCreate):
    global contador
    contador += 1
    nova = {"id": contador, "titulo": tarefa.titulo, "concluida": False}
    tarefas[contador] = nova
    return nova


@app.get("/tarefas")
def listar_tarefas():
    return list(tarefas.values())


@app.get("/tarefas/{id}")
def obter_tarefa(id: int):
    if id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefas[id]


@app.put("/tarefas/{id}")
def atualizar_tarefa(id: int, dados: TarefaUpdate):
    if id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefas[id]["titulo"] = dados.titulo
    tarefas[id]["concluida"] = dados.concluida
    return tarefas[id]


@app.delete("/tarefas/{id}", status_code=204)
def deletar_tarefa(id: int):
    if id not in tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    del tarefas[id]
