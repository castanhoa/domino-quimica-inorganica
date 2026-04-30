import Domino
import random

quantia_total_pedras = 14

def sub_lists(l0:list, l1:list):
    return list( set(l0) - set(l1) )

class Jogo:
    def __init__(self):

        todas_pedras = Domino.obter_todas_pedras(quantia_total_pedras)

        self.monte = random.sample(todas_pedras, quantia_total_pedras // 2) # inicializar o monte
        todas_pedras = sub_lists(todas_pedras, self.monte)

        self.jogador_principal = self.Jogador(jogo=self, apelido="Jogador principal")
        jog_princ_pedras = random.sample(todas_pedras, quantia_total_pedras // 4)
        self.jogador_principal.inicializar_pedras( jog_princ_pedras )
        todas_pedras = sub_lists(todas_pedras, self.jogador_principal.pedras)


        self.jogador_IA = self.Jogador(jogo=self, apelido="Maquina")
        jog_ia_pedras = random.sample(todas_pedras, quantia_total_pedras // 4)
        self.jogador_IA.inicializar_pedras(jog_ia_pedras)
        # todas_pedras = sub_lists(todas_pedras, self.jogador_IA.pedras)

    class Jogador:
        def __init__(self, jogo, apelido):
            self.jogo = jogo
            self.___pedras = []
            self.__apelido = apelido
        
        def inicializar_pedras(self, minhas_pedras:list):
            if len(self.__pedras) == 0:
                self.___pedras = minhas_pedras

        def comprar_pedra(self):
            if len(self.jogo.monte) > 0:
                nova_pedra = (self.jogo.monte.pop(-1))
                self.___pedras.append(nova_pedra)

                print(f"JOGADOR {self.__apelido} COMPROU PEDRA {nova_pedra}")
                
            else:
                print(f"JOGADOR {self.__apelido} TENTOU COMPRAR PEDRA, MAS NAO HA MAIS PEDRAS NO MONTE")

        def inserir_pedra(self, minha_pedra, pedra_conexao):
            pass

