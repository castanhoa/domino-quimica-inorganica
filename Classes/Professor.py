from Usuario import Usuario

class Professor(Usuario):
    def __init__(self, senha:str , nome:str , turmas:list , logado_ao_criar_conta:bool=False):
        super().__init__(senha, nome, logado_ao_criar_conta)
        self.__turmas = turmas

    # esqueleto apenas. nada pronto.
    def ver_turma(id_turma:int):
        pass

    def adicionar_peca(dado_0:str , dado_1:str):
        pass

    def remover_peca(id_peca):
        pass