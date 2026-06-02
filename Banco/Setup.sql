-- SQLite não possui CREATE SCHEMA nem USE
-- O banco é definido pelo arquivo .db conectado pela aplicação

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS pecas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value_0 TEXT NOT NULL,
    value_1 TEXT NOT NULL
);

INSERT INTO pecas (value_1, value_2) VALUES
('Base', 'Acido'),
('Base', 'Base'),
('Base', 'Oxido'),
('Base', 'Sal'),
('Base', 'Sal'),
('Base', 'Oxido'),
('Base', 'Base'),
('Base', 'Acido'),
('Acido', 'Acido'),
('Acido', 'Base'),
('Acido', 'Oxido'),
('Acido', 'Sal'),
('Acido', 'Acido'),
('Acido', 'Base'),
('Acido', 'Oxido'),
('Acido', 'Sal'),
('Sal', 'Acido'),
('Sal', 'Base'),
('Sal', 'Sal'),
('Sal', 'Oxido'),
('Sal', 'Acido'),
('Sal', 'Base'),
('Sal', 'Sal'),
('Sal', 'Oxido'),
('Oxido', 'Acido'),
('Oxido', 'Base'),
('Oxido', 'Sal'),
('Oxido', 'Oxido'),
('Oxido', 'Acido'),
('Oxido', 'Base'),
('Oxido', 'Sal'),
('Oxido', 'Oxido');

CREATE TABLE IF NOT EXISTS sala (
    id_sala INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS aluno (
    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_aluno VARCHAR(75) NOT NULL,
    num_partidas INTEGER DEFAULT 0,
    num_vitorias INTEGER DEFAULT 0
    tempo_jogo TIME DEFAULT '00:00:00'
);