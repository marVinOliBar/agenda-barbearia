from service import (criar_agendamento_service,
                     formatar_agendamentos)


def test_cliente_vazio_e_recusado():
    cliente = ""
    telefone = "17777"
    inicio = "2026-09-29 08:00 "
    
    resultado = criar_agendamento_service(cliente, telefone, inicio)
    
    assert resultado == (False, "O cliente deve ter um nome cadastrado.")
    
def test_cliente_com_espaco_e_recusado():
    cliente = "    "
    telefone = "17777"
    inicio = "2026-09-29 08:00"
    
    resultado = criar_agendamento_service(cliente, telefone, inicio)
    
    assert resultado == (False, "O cliente deve ter um nome cadastrado.")
    
def test_cliente_none_e_recusado():
    resultado = criar_agendamento_service(None, "177777", "2026-09-29 08:00")
    assert resultado == (False, "O cliente deve ter um nome cadastrado.")
    
def test_formatar_remove_cancelados_e_devolve_dicionarios():
    # preparar — as linhas na mão, como se tivessem vindo do banco
    linhas = [
        (1, "joao",  "17999", "2026-09-20 09:00", "agendado"),
        (2, "maria", "17888", "2026-09-20 10:00", "cancelado"),
        (3, "ana",   "17777", "2026-09-20 11:00", "atendido"),
    ]

    # executar
    resultado = formatar_agendamentos(linhas)

    # verificar
    assert resultado == [
        {"id_cliente": 1, "cliente": "joao", "telefone": "17999",
         "inicio": "2026-09-20 09:00", "status": "agendado"},
        {"id_cliente": 3, "cliente": "ana", "telefone": "17777",
         "inicio": "2026-09-20 11:00", "status": "atendido"},
    ]
    
def test_agendamento_data_passada():
    cliente = "marcus"
    telefone = "1798220"
    inicio = "2026-09-15 08:00"
    
    resultado = criar_agendamento_service(cliente, telefone, inicio)
    
    assert resultado == (False, "A data não pode ser anterior ao horario atual.")