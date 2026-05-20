CREATE SCHEMA jogo;
use jogo;
SET FOREIGN_KEY_CHECKS = 1 ;
SET SQL_SAFE_UPDATES = 0 ;
SELECT @@default_storage_engine ;
DROP TABLE IF EXISTS pecas;
CREATE TABLE pecas(
    id TINYINT AUTO_INCREMENT PRIMARY KEY,
    value_1 VARCHAR(5) NOT NULL,
    value_2 VARCHAR(5) NOT NULL
);
INSERT INTO pecas VALUES
(DEFAULT,'Base', 'Acido'),
(DEFAULT,'Base', 'Base'),
(DEFAULT, 'Base', 'Oxido'),
(DEFAULT,'Base', 'Sal'),
(DEFAULT,'Base', 'Sal'),
(DEFAULT,'Base', 'Oxido'),
(DEFAULT,'Base', 'Base'),
(DEFAULT,'Base', 'Acido'),
(DEFAULT,'Acido', 'Acido'),
(DEFAULT,'Acido', 'Base'),
(DEFAULT,'Acido', 'Oxido'),
(DEFAULT,'Acido', 'Sal'),
(DEFAULT,'Acido', 'Acido'),
(DEFAULT,'Acido', 'Base'),
(DEFAULT,'Acido', 'Oxido'),
(DEFAULT, 'Acido', 'Sal'),
(DEFAULT, 'Sal', 'Acido'),
(DEFAULT, 'Sal', 'Base'),
(DEFAULT,'Sal', 'Sal'),
(DEFAULT, 'Sal', 'Oxido'),
(DEFAULT, 'Sal', 'Acido'),
(DEFAULT, 'Sal', 'Base'),
(DEFAULT, 'Sal', 'Sal'),
(DEFAULT, 'Sal', 'Oxido'),
(DEFAULT, 'Oxido', 'Acido'),
(DEFAULT, 'Oxido', 'Base'),
(DEFAULT, 'Oxido', 'Sal'),
(DEFAULT, 'Oxido', 'Oxido'),
(DEFAULT, 'Oxido', 'Acido'),
(DEFAULT, 'Oxido', 'Base'),
(DEFAULT, 'Oxido', 'Sal'),
(DEFAULT, 'Oxido', 'Oxido');
CREATE TABLE sala IF NOT EXISTS (
    id_sala INTEGER PRIMARY KEY,
)
CREATE TABLE aluno IF NOT EXISTS (
    id_aluno INTEGER PRIMARY KEY,
    nome_aluno VARCHAR(70),
    pontuacao INTEGER DEFAULT
)