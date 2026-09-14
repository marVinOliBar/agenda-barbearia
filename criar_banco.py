import sqlite3

conexao = sqlite3.connect("agenda.db")
conexao.executescript(open("schema.sql", encoding="utf-8").read())
conexao.close()
print("banco criado")
