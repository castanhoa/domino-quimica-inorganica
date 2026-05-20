import sqlite3
import logging
from contextlib import contextmanager

# ---------------------------------------------------------------------------
# Configuração do logger
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Caminho do banco de dados
# ---------------------------------------------------------------------------
DB_PATH = "mysql://localhost/root/jogo_peca"

# ---------------------------------------------------------------------------
# Conexão
# ---------------------------------------------------------------------------
@contextmanager
def get_connection(db_path: str = DB_PATH):
    """
    Abre uma conexão com o SQLite e a entrega para o bloco 'with'.
    Ao sair do bloco:
      - sem erros  → commit (salva as alterações)
      - com erro   → rollback (descarta as alterações)
      - sempre     → fecha a conexão
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row          # permite acessar colunas pelo nome
    conn.execute("PRAGMA foreign_keys = ON")  # ativa integridade referencial
    try:
        yield conn          # disponibiliza a conexão para o bloco 'with'
        conn.commit()
    except Exception as e:
        conn.rollback()
        logger.error("Erro na transação, rollback realizado: %s", e)
        raise
    finally:
        conn.close()
# Funções de acesso a dados
def insert(table: str, data: dict) -> int:
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["?"] * len(data))
    values = tuple(data.values())

    with get_connection() as conn:
        cursor = conn.execute(
            f"INSERT INTO {table} ({columns}) VALUES ({placeholders})",
            values,
        )
        return cursor.lastrowid


def dados_alunos(Dado, sala, filters: dict = None) -> list:
    query = f"SELECT nome_aluno, tempo_jogado, num_partidas FROM alunos WHERE id_sala = {sala}"
    params = []

    if filters:
        for column, value in filters.items():
            query += f" AND {column} = ?"

    query += f" ORDER BY {Dado}"

    with get_connection() as conn:
        return conn.execute(query, params).fetchall()


def pegar_valor(table: str, record_id: int) -> list:
    with get_connection() as conn:
        return conn.execute(
            f"SELECT value_1, value_2 FROM {table} WHERE id = ?", (record_id,)
        ).fetchone()


def update(table: str, record_id: int, data: dict) -> None:
    set_clause = ", ".join([f"{col} = ?" for col in data.keys()])
    values = tuple(data.values()) + (record_id,)

    with get_connection() as conn:
        conn.execute(
            f"UPDATE {table} SET {set_clause} WHERE id = ?",
            values,
        )


def delete(table: str, record_id: int) -> None:
    with get_connection() as conn:
        conn.execute(f"DELETE FROM {table} WHERE id = ?", (record_id,))