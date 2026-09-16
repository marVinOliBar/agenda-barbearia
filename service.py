import sqlite3
from storage import (criar_agendamento_storage,
                     listar_agendamentos_storage,)

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

def listar_agendamento_service():
    
    linhas = listar_agendamentos_storage()
    formatados = formatar_agendamentos(linhas)
        
    return (True, formatados)

def formatar_agendamentos(linhas):
    
    return [{'id_cliente': identidade, 'cliente': nome, 'telefone': fone, 'inicio': horario, 'status': estado} for identidade, nome, fone, horario, estado in linhas if estado != 'cancelado']