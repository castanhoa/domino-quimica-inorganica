from Usuario import Usuario

class Aluno(Usuario):
    def __init__(self, senha:str , nome:str , id_turma:int , logado_ao_criar_conta:bool=False):
        super().__init__(senha, nome, logado_ao_criar_conta)
        self.__id_turma = id_turma
        self.__taxa_vitoria = 1

    # esqueleto apenas. nada pronto.
    def ver_estatisticas():
        pass