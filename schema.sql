CREATE TABLE agendamento(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT NOT NULL,
    telefone TEXT NOT NULL,
    inicio TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL DEFAULT 'agendado'
    CHECK (status IN ('agendado', 'atendido', 'cancelado'))
);