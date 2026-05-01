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
DB_PATH = "app.db"

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


def fetch_all(table: str, filters: dict = None, limit: int = 100) -> list:
    query = f"SELECT * FROM {table} WHERE 1=1"
    params = []

    if filters:
        for column, value in filters.items():
            query += f" AND {column} = ?"
            params.append(value)

    query += f" ORDER BY id DESC LIMIT ?"
    params.append(limit)

    with get_connection() as conn:
        return conn.execute(query, params).fetchall()


def fetch_one(table: str, record_id: int) -> sqlite3.Row:
    with get_connection() as conn:
        return conn.execute(
            f"SELECT * FROM {table} WHERE id = ?", (record_id,)
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


# ---------------------------------------------------------------------------
# Exemplo de uso (execução direta)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    init_db()

    id1 = insert("events", {"event_type": "clique",    "description": "Botão salvar pressionado", "user_id": 1})
    id2 = insert("events", {"event_type": "navegacao", "description": "Tela de relatórios aberta", "user_id": 1})
    id3 = insert("events", {"event_type": "clique",    "description": "Botão cancelar pressionado", "user_id": 2})

    print("\n--- Eventos do tipo 'clique' ---")
    for row in fetch_all("events", filters={"event_type": "clique"}):
        print(dict(row))

    print("\n--- Evento id=2 ---")
    print(dict(fetch_one("events", id2)))

    update("events", id1, {"description": "Botão salvar — atualizado"})
    delete("events", id3)

    print("\n--- Todos os eventos ---")
    for row in fetch_all("events"):
        print(dict(row))