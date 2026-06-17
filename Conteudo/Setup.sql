CREATE SCHEMA bd_jogo_domino_quimica;
USE bd_jogo_domino_quimica;
 
SET FOREIGN_KEY_CHECKS = 1 ;
SET SQL_SAFE_UPDATES = 0 ;
SELECT @@default_storage_engine ;

DROP TABLE IF EXISTS pecas ;

CREATE TABLE IF NOT EXISTS pecas( 
    id SMALLINT AUTO_INCREMENT PRIMARY KEY, 
    dado_0 VARCHAR(5) NOT NULL, 
    dado_1 VARCHAR(5) NOT NULL 
);

INSERT INTO pecas (dado_0, dado_1) VALUES
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
    id_aluno INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome_aluno VARCHAR(75) NOT NULL,
    num_partidas INTEGER DEFAULT 0,
    num_vitorias INTEGER DEFAULT 0,
    tempo_jogo TIME DEFAULT '00:00:00'
    email VARCHAR(75)
    senha: VARCHAR(20)
);

