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

CREATE TABLE IF NOT EXISTS turma (
    id_turma INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS aluno (
    nome_aluno VARCHAR(75) NOT NULL,
    
    email_aluno VARCHAR(75) NOT NULL,
    hash_senha_aluno CHAR(64) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
    
    partidas_jogadas_aluno INTEGER DEFAULT 0,
    partidas_jogadas_vencidas_aluno INTEGER DEFAULT 0,
    
    tentativas_conexao_aluno INTEGER DEFAULT 0,
    tentativas_conexao_corretas_aluno INTEGER DEFAULT 0,
    
    tempo_total_jogado_aluno FLOAT DEFAULT 0.0,
    
	id_aluno INTEGER PRIMARY KEY AUTO_INCREMENT

);


CREATE TABLE IF NOT EXISTS professor (
    nome_prof VARCHAR(75) NOT NULL,
    
    email_prof VARCHAR(75) NOT NULL,
    hash_senha_prof CHAR(64) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
    
	id_prof INTEGER PRIMARY KEY AUTO_INCREMENT

);

-- Para fins de testes
INSERT INTO aluno VALUES(
"Balduíno Andrades da Silva",
"123@aluno.cps.sp.gov.br",
"a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",
DEFAULT,
DEFAULT,
DEFAULT,
DEFAULT,
DEFAULT,
DEFAULT
);

INSERT INTO professor VALUES (
"Rogério Matos Rei",
"456@cps.sp.gov.br",
"b3a8e0e1f9ab1bfe3a36f231f676f78bb30a519d2b21e6c530c0eee8ebb4a5d0",
DEFAULT
);