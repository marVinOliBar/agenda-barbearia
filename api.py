from typing import Annotated

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from service import listar_agendamento_service, criar_agendamento_service

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class NovoAgendamento(BaseModel):
    cliente: str
    telefone: str
    inicio: str

@app.get("/")
def pagina_inicial(request: Request):
    _, agendamentos = listar_agendamento_service()
    return templates.TemplateResponse(request=request, name="index.html", context={"agendamentos": agendamentos})

@app.get("/agendamentos")
def listar_agendamentos():
    _, agendamentos = listar_agendamento_service()
    return agendamentos

@app.post("/agendamentos")
def criar_agendamento(dados: Annotated[NovoAgendamento, Form()]):
    sucesso, resultado = criar_agendamento_service(dados.cliente, dados.telefone, dados.inicio)
    if not sucesso:
        raise HTTPException(status_code=400, detail=resultado)
    return RedirectResponse(url="/", status_code=303)