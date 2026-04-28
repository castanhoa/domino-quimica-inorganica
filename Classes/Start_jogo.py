

class Jogo:
    def __init__(self):
        self.monte = [] # inicializar o monte
        self.jogador_principal = self.Jogador(jogo=self, apelido="Jogador principal")
        self.jogador_IA = self.Jogador(jogo=self, apelido="Maquina")

    class Jogador:
        def __init__(self, jogo, apelido):
            self.jogo = jogo
            self.pedras = []
            self.apelido = apelido

        def comprar_pedra(self):
            if len(self.jogo.monte) > 0:
                nova_pedra = (self.jogo.monte.pop(-1))
                self.pedras.append(nova_pedra)

                print(f"JOGADOR {self.apelido} COMPROU PEDRA {nova_pedra}")
                
            else:
                print(f"JOGADOR {self.apelido} TENTOU COMPRAR PEDRA, MAS NAO HA MAIS PEDRAS NO MONTE")

        def inserir_pedra(self, minha_pedra, pedra_conexao):
            pass

