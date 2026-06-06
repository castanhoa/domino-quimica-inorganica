from Usuario import Usuario

from math import e as eulers

def sigmoid_var(x):
    return 1 / (1 + eulers**(-x-0.5))

class Aluno(Usuario):
    def __init__(self, senha:str , nome:str , id_turma:int , logado_ao_criar_conta:bool=False):
        super().__init__(senha, nome, logado_ao_criar_conta)
        self.__partidas_jogadas = 1
        self.__partidas_jogadas_vencidas = 0

        self.__tentativas_conexao = 1
        self.__tentativas_conexao_corretas = 0


    def get_estatisticas(self):

        estatisticas_partidas = []

        estatisticas_partidas.append(self.__partidas_jogadas_vencidas)
        estatisticas_partidas.append(self.__partidas_jogadas)
        estatisticas_partidas.append(self.__partidas_jogadas_vencidas / self.__partidas_jogadas)

        #----#

        estatisticas_tentativas_conexao = []

        estatisticas_tentativas_conexao.append(self.__tentativas_conexao_corretas)
        estatisticas_tentativas_conexao.append(self.__tentativas_conexao)
        estatisticas_tentativas_conexao.append(self.__tentativas_conexao_corretas / self.__tentativas_conexao)

        return estatisticas_partidas, estatisticas_tentativas_conexao
    
    def obter_dificuldade(self):
        stats_partidas, stats_tentativas_conexao = self.get_estatisticas()

        return sigmoid_var(stats_partidas[2] + stats_tentativas_conexao[2])

    def resultado(self, victory:bool, tentativas_conexao_partida:int, tentativas_conexao_corretas_partida:int):
        self.__partidas_jogadas +=1
        if victory:
            self.__partidas_jogadas_vencidas +=1

        self.__tentativas_conexao += tentativas_conexao_partida
        self.__tentativas_conexao_corretas += tentativas_conexao_corretas_partida