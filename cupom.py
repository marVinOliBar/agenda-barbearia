from datetime import datetime

validade_texto = "2026-09-15 08:00"

validade = datetime.strptime(validade_texto, "%Y-%m-%d %H:%M")
agora = datetime.now()

print(validade)
print(type(validade))
print(validade < agora)