from service import criar_agendamento_service


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