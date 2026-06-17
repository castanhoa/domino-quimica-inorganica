import os
from contextlib import contextmanager
from typing import List, Optional

from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


def obter_url_banco() -> str:
    """Monta a URL do MySQL a partir das variaveis de ambiente.

    Exemplo:
    set DB_USER=root
    set DB_PASSWORD=senha
    set DB_HOST=localhost
    set DB_PORT=3306
    set DB_NAME=bd_jogo_domino_quimica
    """
    usuario = os.getenv("DB_USER", "root")
    senha = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "localhost")
    porta = os.getenv("DB_PORT", "3306")
    nome_banco = os.getenv("DB_NAME", "bd_jogo_domino_quimica")

    return f"mysql+pymysql://{usuario}@{host}:{porta}/{nome_banco}"


class Base(DeclarativeBase):
    pass


class Peca(Base):
    __tablename__ = "pecas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    dado_0: Mapped[str] = mapped_column(String(100), nullable=False)
    dado_1: Mapped[str] = mapped_column(String(100), nullable=False)


class Aluno(Base):
    __tablename__ = "aluno"

    id_aluno: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome_aluno: Mapped[str] = mapped_column(String(75), nullable=False)
    num_partidas: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    num_vitorias: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    tempo_jogo: Mapped[str] = mapped_column(String(20), default="00:00:00", nullable=False)
    email : Mapped[str]  = mapped_column(String(75), nullable = False)
    senha : Mapped[str] = mapped_column(String(20), nullable = False)

engine = create_engine(obter_url_banco(), echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def criar_tabelas() -> None:
    Base.metadata.create_all(bind=engine)


@contextmanager
def obter_sessao():
    sessao = SessionLocal()
    try:
        yield sessao
        sessao.commit()
    except Exception:
        sessao.rollback()
        raise
    finally:
        sessao.close()


def adicionar_peca(record_id: int) -> Optional[tuple[str, str]]:
    """Retorna (dado_0, dado_1) da peca pelo id ou None se nao existir."""
    with obter_sessao() as sessao:
        peca = sessao.get(Peca, record_id)
        if peca is None:
            return None
        return (peca.dado_0, peca.dado_1)


def listar_pecas() -> List[Peca]:
    """Lista todas as peças do banco."""
    with obter_sessao() as sessao:
        return list(sessao.query(Peca).all())


def pegar_valor(table: str, record_id: int) -> Optional[List[str]]:
    """Retorna [dado_0, dado_1] para a tabela 'pecas'."""
    tabelas_permitidas = {
        "pecas": Peca,
    }

    modelo = tabelas_permitidas.get(table)
    if modelo is None:
        raise ValueError(f"Tabela nao permitida: {table}")

    with obter_sessao() as sessao:
        instancia = sessao.get(modelo, record_id)
        if instancia is None:
            return None
        return [instancia.dado_0, instancia.dado_1]


def pegar_dados_alunos(dado_determinante: str, id_turma: int = None) -> List[list]:
    """Retorna lista de alunos com seus dados determinantes, ordenados alfabeticamente."""
    with obter_sessao() as sessao:
        query = sessao.query(Aluno)
        if id_turma is not None:
            query = query.filter(Aluno.id_turma == id_turma)
        alunos = query.order_by(Aluno.nome_aluno).all()
        return [[aluno.nome_aluno, getattr(aluno, dado_determinante, None)] for aluno in alunos]


def pegar_instancia_alunos(id_aluno: int, lista: List) -> Optional[object]:
    """Retorna instância do aluno da lista que corresponde ao id_aluno do banco."""
    with obter_sessao() as sessao:
        aluno = sessao.query(Aluno).filter(Aluno.id_aluno == id_aluno).first()
        if aluno is None:
            raise ValueError(f"aluno não encontrado com id {id_aluno}")
        for obj in lista:
            if aluno.nome_aluno == getattr(obj, 'nome', None):
                return obj
        return "Erro"


def inicializar_pedra(id_pedra: int) -> Optional[tuple[str, str]]:
    """Retorna (dado_0, dado_1) da peça pelo id."""
    with obter_sessao() as sessao:
        peca = sessao.get(Peca, id_pedra)
        if peca is None:
            raise ValueError(f"Peca com id {id_pedra} nao encontrada")
        return (peca.dado_0, peca.dado_1)


def pegar_dados_aluno(id_aluno: int) -> str:
    """Retorna string formatada com estatísticas do aluno."""
    with obter_sessao() as sessao:
        aluno = sessao.query(Aluno).filter(Aluno.id_aluno == id_aluno).first()
        if aluno is None:
            raise ValueError(f"aluno não encontrado com id {id_aluno}")
        return f"{aluno.nome_aluno}, jogos: {aluno.num_partidas}, vitorias {aluno.num_vitorias}, tempo: {aluno.tempo_jogo}"


def atualizar(id_aluno: int, tempo_segundos: int, resultado: bool) -> str:
    """Atualiza estatisticas do aluno: incrementa partidas, vitorias e soma tempo.

    tempo_segundos: número de segundos a adicionar ao tempo_jogo.
    """
    def to_seconds(tstr: str) -> int:
        try:
            h, m, s = map(int, tstr.split(":"))
            return h * 3600 + m * 60 + s
        except Exception:
            return 0

    def to_hms(sec: int) -> str:
        h = sec // 3600
        m = (sec % 3600) // 60
        s = sec % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    with obter_sessao() as sessao:
        aluno = sessao.query(Aluno).filter(Aluno.id_aluno == id_aluno).first()
        if aluno is None:
            return "Problema"

        current = to_seconds(aluno.tempo_jogo or "00:00:00")
        total = current + int(tempo_segundos)
        aluno.tempo_jogo = to_hms(total)
        aluno.num_partidas = (aluno.num_partidas or 0) + 1
        aluno.num_vitorias = (aluno.num_vitorias or 0) + (1 if resultado else 0)

        sessao.add(aluno)
        return "Atualizada com sucesso"

def buscar_senha(correio: string):
    with obter_sessao as sessao:
        seguranca  = sessao.query(Aluno).filter(correio == Aluno.email).senha
        return seguranca