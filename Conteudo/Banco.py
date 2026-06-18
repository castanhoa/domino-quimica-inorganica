import os
from contextlib import contextmanager

from sqlalchemy import CHAR, Float, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

from Conteudo.Aluno import Aluno as AlunoBackend


def obter_url_banco() -> str:
    """
    Monta a URL do MySQL a partir das variaveis de ambiente.

    Exemplo:
    set DB_USER=root
    set DB_PASSWORD=senha
    set DB_HOST=localhost
    set DB_PORT=3306
    set DB_NAME=bd_jogo_domino_quimica
    """
    usuario = os.getenv("DB_USER", "root")
    senha = os.getenv("DB_PASSWORD", "Yoshi574$$")
    host = os.getenv("DB_HOST", "localhost")
    porta = os.getenv("DB_PORT", "3306")
    nome_banco = os.getenv("DB_NAME", "bd_jogo_domino_quimica")

    return f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{nome_banco}"


class Base(DeclarativeBase):
    pass


class Turma(Base):
    __tablename__ = "turma"

    id_turma: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


class Aluno(Base):
    __tablename__ = "aluno"

    # id_aluno: Mapped[int] = mapped_column(
    #     Integer,
    #     primary_key=True,
    #     autoincrement=True
    # )

    nome_aluno: Mapped[str] = mapped_column(
        String(75),
        nullable=False
    )

    email_aluno: Mapped[str] = mapped_column(
        String(75),
        nullable=False,
        primary_key=True

    )

    hash_senha_aluno: Mapped[str] = mapped_column(
        CHAR(64),
        nullable=False
    )

    partidas_jogadas_aluno: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    partidas_jogadas_vencidas_aluno: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    tentativas_conexao_aluno: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    tentativas_conexao_corretas_aluno: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    tempo_total_jogado_aluno: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )


class Professor(Base):
    __tablename__ = "professor"

    nome_prof: Mapped[str] = mapped_column(
        String(75),
        nullable=False
    )

    email_prof: Mapped[str] = mapped_column(
        String(75),
        nullable=False,
        primary_key=True

    )

    hash_senha_prof: Mapped[str] = mapped_column(
        CHAR(64),
        nullable=False
    )


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


def adicionar_peca(meu_id) -> Peca:
    with obter_sessao() as sessao:
        peca = sessao.query(Peca).filter_by(meu_id==id).first()
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
    
# ARRUMAR
def pegar_instancia_alunos(id_aluno, lista):
        with obter_sessao() as sessao:
            aluno = sessao.query(Aluno).filter(Aluno.id == id_aluno)
            if aluno is None:
                raise ValueError(f"aluno não encontrado com id {id_aluno}")
            for obj in lista:
                if aluno.nome == obj.nome:
                    return obj
            return "Erro"


def inicializar_pedra(id_pedra):
    with obter_sessao() as sessao:
        peca = sessao.query(peca).filter_by(id=id_pedra).first()
        if peca is None:
            raise ValueError(f"Peca com id {id_pedra} nao encontrada")
        return (peca.value_0, peca.value_1)
    
def ver_existencia_de_aluno(email_alvo):
    with obter_sessao() as sessao:
        stmt = select(Aluno).where(Aluno.email_aluno == email_alvo).exists()

        return sessao.scalar(select(stmt))
    
def ver_existencia_de_professor(email_alvo):
    with obter_sessao() as sessao:
        stmt = select(Professor).where(Professor.email_prof == email_alvo).exists()

        return sessao.scalar(select(stmt))

def pegar_dados_aluno(email_aluno):
    with obter_sessao() as sessao:
        aluno = sessao.query(Aluno).filter(Aluno.email_aluno == email_aluno).first()
        if aluno is None:
            raise ValueError(f"aluno não encontrado com email {email_aluno}")
        
        return aluno.partidas_jogadas_aluno, aluno.partidas_jogadas_vencidas_aluno, aluno.tentativas_conexao_aluno, aluno.tentativas_conexao_corretas_aluno, aluno.tempo_total_jogado_aluno
    

def atualizar(objAluno):
    email_aluno = objAluno.get_username()

    with obter_sessao() as sessao:
        update = sessao.query(Aluno).filter_by(email_aluno=Aluno.email_aluno).first()
        if update and isinstance(objAluno, AlunoBackend):
            
            partidas_jogadas_aluno, partidas_jogadas_vencidas_aluno, tentativas_conexao_aluno,tentativas_conexao_corretas_aluno, tempo_total_jogado_aluno = objAluno.get_dados_jogatinas()

            update.partidas_jogadas_aluno = partidas_jogadas_aluno
            update.partidas_jogadas_vencidas_aluno = partidas_jogadas_vencidas_aluno
            update.tentativas_conexao_aluno = tentativas_conexao_aluno
            update.tentativas_conexao_corretas_aluno = tentativas_conexao_corretas_aluno
            update.tempo_total_jogado_aluno = tempo_total_jogado_aluno

            sessao.commit()
            return "Atualizada com sucesso"
        else:
            return "Problema"

def buscar_senha(correio: str, e_aluno:bool):
    with obter_sessao() as sessao:
        if e_aluno == True:
            seguranca = sessao.query(Aluno).filter(correio == Aluno.email_aluno).first().hash_senha_aluno

        elif e_aluno == False:
            seguranca = sessao.query(Professor).filter(correio == Professor.email_prof).hash_senha_prof
      
        else:
            raise(Exception, "Lógica ternária não!")

        return seguranca