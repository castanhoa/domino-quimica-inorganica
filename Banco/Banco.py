import os
from contextlib import contextmanager

from sqlalchemy import Boolean, ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker


def obter_url_banco() -> str:
    """
    Monta a URL do MySQL a partir das variaveis de ambiente.

    Exemplo:
    set DB_USER=root
    set DB_PASSWORD=senha
    set DB_HOST=localhost
    set DB_PORT=3306
    set DB_NAME=domino_quimica
    """
    usuario = os.getenv("DB_USER", "root")
    senha = os.getenv("DB_PASSWORD", "tinCTrom")
    host = os.getenv("DB_HOST", "localhost")
    porta = os.getenv("DB_PORT", "3306")
    nome_banco = os.getenv("DB_NAME", "domino_quimica")

    return f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{nome_banco}"


class Base(DeclarativeBase):
    pass


class Turma(Base):
    __tablename__ = "turmas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)

    alunos: Mapped[list["Aluno"]] = relationship(back_populates="turma")


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome_hash: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    senha_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    logado: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    pontuacao_total: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    tipo: Mapped[str] = mapped_column(String(20), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "usuario",
        "polymorphic_on": tipo,
    }


class Aluno(Usuario):
    __tablename__ = "alunos"

    id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), primary_key=True)
    id_turma: Mapped[int] = mapped_column(ForeignKey("turmas.id"), nullable=False)
    partidas_jogadas: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    partidas_vencidas: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    dificuldade: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    turma: Mapped[Turma] = relationship(back_populates="alunos")

    __mapper_args__ = {
        "polymorphic_identity": "aluno",
    }


class Professor(Usuario):
    __tablename__ = "professores"

    id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "professor",
    }


class Peca(Base):
    __tablename__ = "pecas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    dado_0: Mapped[str] = mapped_column(String(100), nullable=False)
    dado_1: Mapped[str] = mapped_column(String(100), nullable=False)


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


def adicionar_peca(self, id) -> Peca:
    with obter_sessao() as sessao:
        peca = sessao.query(Peca).filter_by(self.id == id).first()
        return (peca.valor_0, peca.valor1)


def listar_pecas() -> list[Peca]:
    with obter_sessao() as sessao:
        return list(sessao.query(Peca).all())
    
def pegar_valor(table: str, record_id: int) -> list | None:
    tabelas_permitidas = {
        "pecas": Peca,
    }

    modelo = tabelas_permitidas.get(table)
    if modelo is None:
        raise ValueError(f"Tabela nao permitida: {table}")

    with obter_sessao() as sessao:
        resultado = sessao.execute(
            select(modelo.dado_0, modelo.dado_1).where(modelo.id == record_id)
        ).one_or_none()

        if resultado is None:
            return None

        return [resultado.dado_0, resultado.dado_1]
def pegar_dados_alunos(dado_determinante: String, id_turma: int) -> list[Aluno]:
    with obter_sessao() as sessao:
        alunos = sessao.query(Aluno).filter(Aluno.id_turma == id_turma).order_by(Aluno.dado_dado_determinante.desc()).all()
        return [[
                aluno.nome_aluno,
                aluno.dado_dado_determinante,
            ]
            for aluno in alunos
            ]
    
def inicializar_pedra(id_pedra):
    with obter_sessao() as sessao:
        peca = sessao.query(Peca).filter_by(id=id_pedra).first()
        if peca is None:
            raise ValueError(f"Peca com id {id_pedra} nao encontrada")
        return (peca.value_0, peca.value_1)
    