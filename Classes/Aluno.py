from Usuario import Usuario

class Aluno(Usuario):
    def __init__(self, senha:str , nome:str , id_turma:int , logado_ao_criar_conta:bool=False):
        super().__init__(senha, nome, logado_ao_criar_conta)
        self.__id_turma = id_turma
        self.__taxa_vitoria = 1
        self.__partidas_jogadas = 0
        self.__dificuldade = 0
        self.__partidas_vencidas = 0
    # esqueleto apenas. nada pronto.
    def ver_estatisticas(self):
        self.__taxa_vitoria = self.__partidas_jogadas/self.__partidas_vencidas
        return self.__taxa_vitoria
    def resultado(self, victory:bool):
        self.__partidas_jogadas +=1
        if victory:
            self.__partidas_vencidas +=1
