from fastapi import FastAPI
from pydantic import BaseModel
from service import listar_agendamento_service, criar_agendamento_service

app = FastAPI()

class NovoAgendamento(BaseModel):
    cliente: str
    telefone: str
    inicio: str

@app.get("/agendamentos")
def listar_agendamentos():
    _, agendamentos = listar_agendamento_service()
    return agendamentos

@app.post("/agendamentos")
def criar_agendamento(dados: NovoAgendamento):
    sucesso, resultado = criar_agendamento_service(dados.cliente, dados.telefone, dados.inicio)
    if sucesso:
        return {"sucesso": True, "id": resultado}
    return {"sucesso": False, "mensagem": resultado}