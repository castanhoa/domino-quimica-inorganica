from Conteudo.Usuario import Usuario

from math import e as eulers

def sigmoid_var(x):
    return 1 / (1 + eulers**(-x-0.5))

class Aluno(Usuario):
    def __init__(self, senha:str , nome:str , logado_ao_criar_conta:bool=False):
        super().__init__(senha, nome, logado_ao_criar_conta)
        self.__partidas_jogadas = 1
        self.__partidas_jogadas_vencidas = 0

        self.__tentativas_conexao = 1
        self.__tentativas_conexao_corretas = 0

        self.__tempo_total_jogado = 0.0

        self.__dados_carregados = False

    def set_dados_jogatinas(self, partidas_jogadas, partidas_jogadas_vencidas, tentativas_conexao, tentativas_conexao_corretas, tempo_total_jogado):
        if self.__dados_carregados != False:
            return

        self.__dados_carregados = True

        self.__partidas_jogadas = partidas_jogadas
        self.__partidas_jogadas_vencidas = partidas_jogadas_vencidas

        self.__tentativas_conexao = tentativas_conexao
        self.__tentativas_conexao_corretas = tentativas_conexao_corretas

        self.__tempo_total_jogado = tempo_total_jogado


    def get_dados_jogatinas(self):
        return self.__partidas_jogadas, self.__partidas_jogadas_vencidas, self.__tentativas_conexao, self.__tentativas_conexao_corretas, self.__tempo_total_jogado

    def get_estatisticas(self):

        estatisticas_partidas = []

        estatisticas_partidas.append(self.__partidas_jogadas_vencidas)
        estatisticas_partidas.append(self.__partidas_jogadas)
        estatisticas_partidas.append(self.__partidas_jogadas_vencidas / max(1, self.__partidas_jogadas))

        #----#

        estatisticas_tentativas_conexao = []

        estatisticas_tentativas_conexao.append(self.__tentativas_conexao_corretas)
        estatisticas_tentativas_conexao.append(self.__tentativas_conexao)
        estatisticas_tentativas_conexao.append(self.__tentativas_conexao_corretas / max(1, self.__tentativas_conexao))

        #----#

        estatisticas_tempo = []

        estatisticas_tempo.append(self.__tempo_total_jogado)
        estatisticas_tempo.append(self.__tempo_total_jogado / max(1, self.__partidas_jogadas))


        return estatisticas_partidas, estatisticas_tentativas_conexao, estatisticas_tempo
    
    def obter_dificuldade(self):
        stats_partidas, stats_tentativas_conexao, _ = self.get_estatisticas()

        return sigmoid_var(stats_partidas[2] + stats_tentativas_conexao[2])

    def resultado(self, victory:bool, tentativas_conexao_partida:int, tentativas_conexao_corretas_partida:int, delta_t):
        self.__partidas_jogadas +=1
        if victory:
            self.__partidas_jogadas_vencidas +=1

        self.__tentativas_conexao += tentativas_conexao_partida
        self.__tentativas_conexao_corretas += tentativas_conexao_corretas_partida

        self.__tempo_total_jogado += delta_t
