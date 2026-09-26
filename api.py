from fastapi import FastAPI
from service import listar_agendamento_service

app = FastAPI()

@app.get("/agendamentos")
def listar_agendamentos():
    _, agendamentos = listar_agendamento_service()
    return agendamentos