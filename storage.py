import sqlite3

CAMINHO_BD = "agenda.db"

def criar_agendamento_storage(cliente, telefone, inicio):
    con = sqlite3.connect(CAMINHO_BD)
    cursor = con.cursor()
    try:
        cursor.execute("INSERT INTO agendamento (cliente, telefone, inicio) VALUES (?, ?, ?)", (cliente, telefone, inicio))
        valor_id = cursor.lastrowid
        con.commit()
    finally:
        con.close()
    return valor_id

def listar_agendamentos_storage():
    con = sqlite3.connect(CAMINHO_BD)
    cursor = con.cursor()
    try:
        cursor.execute("SELECT id, cliente, telefone, inicio, status FROM agendamento ORDER BY inicio")
        resultado = cursor.fetchall()
    finally:
        con.close()
    return resultado