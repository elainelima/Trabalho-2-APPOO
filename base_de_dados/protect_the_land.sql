CREATE TABLE IF NOT EXISTS green_map (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    pontuacao TEXT NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS graveyard_map (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    pontuacao TEXT NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);
