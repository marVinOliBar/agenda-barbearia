import sqlite3
from storage import (criar_agendamento_storage)

def criar_agendamento_service(cliente, telefone, inicio):
    
    cliente = (cliente or "").strip()
    telefone = (telefone or "").strip()
    inicio = (inicio or "").strip()
    
    if not cliente:
        return (False, "O cliente deve ter um nome cadastrado.")
    
    if not telefone:
        return (False, "O cliente deve ter um telefone cadastrado.")
    
    if not inicio:
        return (False, "O cliente deve ter um horário cadastrado.")
    
        
    try:
        resultado = criar_agendamento_storage(cliente, telefone, inicio)
    except sqlite3.IntegrityError:
        return (False, "Esse horário já está ocupado.")
    
    return (True, resultado)