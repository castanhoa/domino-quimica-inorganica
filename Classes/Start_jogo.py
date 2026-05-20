import Domino
import random
import copy
import time

quantia_total_pedras = 28

def sub_lists(l0:list, l1:list):
    return list( set(l0) - set(l1) )

def conversor_extremidade_to_cima(extremidade:int):
    return True if extremidade >= 0 else False

def conectar_pedras(pedra_a, pedra_a_valor_0,  pedra_b, pedra_b_valor_0, conectar_acima:bool, tabuleiro:list):

    pedra_a.pedras_conectadas.append(pedra_b)
    pedra_b.pedras_conectadas.append(pedra_a)

    if pedra_a_valor_0 == True:
        if pedra_b_valor_0 == True:
            pedra_a.valor_0_conexao = pedra_b.valor_0
            pedra_b.valor_0_conexao = pedra_a.valor_0
        else:
            pedra_a.valor_0_conexao = pedra_b.valor_1
            pedra_b.valor_1_conexao = pedra_a.valor_0    
    else:
        if pedra_b_valor_0 == True:
            pedra_a.valor_1_conexao = pedra_b.valor_0
            pedra_b.valor_0_conexao = pedra_a.valor_1
        else:
            pedra_a.valor_1_conexao = pedra_b.valor_1
            pedra_b.valor_1_conexao = pedra_a.valor_1   

    if pedra_b not in tabuleiro:
        raise(ValueError("Pedra b (pedra conexão) não está no tabuleiro."))

    local_pedra_b = tabuleiro.index(pedra_b)

    if conectar_acima == True:
        tabuleiro.insert(local_pedra_b, pedra_a)
    else:
        tabuleiro.insert(local_pedra_b+1, pedra_a)

class Jogo:
    def __init__(self):

        self.todas_pedras_originais = Domino.obter_todas_pedras()
        todas_pedras = copy.copy(self.todas_pedras_originais)

        self.tabuleiro = random.sample(todas_pedras, 1)
        todas_pedras = sub_lists(todas_pedras, self.tabuleiro)

        self.monte = random.sample(todas_pedras, quantia_total_pedras // 2) # inicializar o monte
        todas_pedras = sub_lists(todas_pedras, self.monte)

        self.jogador_principal = self.Jogador(jogo=self, apelido="Jogador principal")
        jog_princ_pedras = random.sample(todas_pedras, quantia_total_pedras // 4)
        self.jogador_principal.inicializar_pedras( jog_princ_pedras )
        todas_pedras = sub_lists(todas_pedras, self.jogador_principal.get_pedras())


        self.jogador_IA = self.Jogador(jogo=self, apelido="Maquina")
        jog_ia_pedras = random.sample(todas_pedras, quantia_total_pedras // 4)
        self.jogador_IA.inicializar_pedras(jog_ia_pedras)
        todas_pedras = sub_lists(todas_pedras, self.jogador_IA.get_pedras())


    class Jogador:
        def __init__(self, jogo, apelido):
            self.jogo = jogo
            self.__pedras = []
            self.__apelido = apelido
        
        def inicializar_pedras(self, minhas_pedras:list):
            if len(self.__pedras) == 0:
                self.___pedras = minhas_pedras

        def get_pedras(self):
            return copy.copy(self.___pedras)
        
        def jogada_ia(self):
            tabuleiro = self.jogo.tabuleiro

            pedra_extremidade_0 = tabuleiro[0]
            pedra_extremidade_1 = tabuleiro[-1]

            possiveis_jogadas = []
            
            for indice_minha_pedra, minha_pedra in enumerate(self.___pedras):
                if Domino.deep_e_compativel(minha_pedra, pedra_extremidade_0):
                    possivel_jogada = {
                        'indice_minha_pedra': indice_minha_pedra, 
                        'pedra_alvo': pedra_extremidade_0,
                        'cima': True,
                                       }
                    
                    possiveis_jogadas.append(possivel_jogada)

                elif Domino.deep_e_compativel(minha_pedra, pedra_extremidade_1):
                    possivel_jogada = {
                        'indice_minha_pedra': indice_minha_pedra, 
                        'pedra_alvo': pedra_extremidade_1,
                        'cima': False,
                                       }                    
                    possiveis_jogadas.append(possivel_jogada)

            if len(possiveis_jogadas) > 0:
                jogada_escolhida = random.choice(possiveis_jogadas)

                indice_minha_pedra = jogada_escolhida['indice_minha_pedra']
                pedra_conexao = jogada_escolhida['pedra_alvo']
                cima = jogada_escolhida['cima']
                 
                self.inserir_pedra(indice_minha_pedra=indice_minha_pedra, pedra_conexao=pedra_conexao, extremidade=(cima))
                
                return True
            else:
                return False

        def comprar_pedra(self):
            if len(self.jogo.monte) > 0:
                nova_pedra = (self.jogo.monte.pop(-1))
                self.___pedras.append(nova_pedra)

                print(f"JOGADOR {self.__apelido} COMPROU PEDRA {nova_pedra}")
                
            else:
                print(f"JOGADOR {self.__apelido} TENTOU COMPRAR PEDRA, MAS NAO HA MAIS PEDRAS NO MONTE")

        def inserir_pedra(self, indice_minha_pedra, pedra_conexao, extremidade:int):
            
            tabuleiro = self.jogo.tabuleiro

            extremidade = 0 if extremidade >= 0 else -1

            cima = extremidade == 0

            minha_pedra = self.___pedras[indice_minha_pedra]

            dupla = minha_pedra.valor_0 == minha_pedra.valor_1

            # eita codigo ineficiente. devera ser melhorado.

            if (pedra_conexao.valor_0_conexao == None):
                if Domino.e_compativel(minha_pedra.valor_0, pedra_conexao.valor_0) == True:
                    conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=True, pedra_b=pedra_conexao, pedra_b_valor_0=True, conectar_acima=cima, tabuleiro=tabuleiro)

                    if dupla == True:
                        conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=False, pedra_b=pedra_conexao, pedra_b_valor_0=True, conectar_acima=cima, tabuleiro=tabuleiro)  
                
                elif Domino.e_compativel(minha_pedra.valor_1, pedra_conexao.valor_0) == True:
                    conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=False, pedra_b=pedra_conexao, pedra_b_valor_0=True, conectar_acima=cima, tabuleiro=tabuleiro)

                    if dupla == True:
                        conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=True, pedra_b=pedra_conexao, pedra_b_valor_0=True, conectar_acima=cima, tabuleiro=tabuleiro)

            elif (pedra_conexao.valor_1_conexao == None):
                if Domino.e_compativel(minha_pedra.valor_0, pedra_conexao.valor_1) == True:
                    conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=True, pedra_b=pedra_conexao, pedra_b_valor_0=False, conectar_acima=cima, tabuleiro=tabuleiro)

                    if dupla == True:
                        conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=True, pedra_b=pedra_conexao, pedra_b_valor_0=False, conectar_acima=cima, tabuleiro=tabuleiro)
                
                elif Domino.e_compativel(minha_pedra.valor_1, pedra_conexao.valor_1) == True:
                    conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=False, pedra_b=pedra_conexao, pedra_b_valor_0=False, conectar_acima=cima, tabuleiro=tabuleiro)

                    if dupla == True:
                        conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=True, pedra_b=pedra_conexao, pedra_b_valor_0=False, conectar_acima=cima, tabuleiro=tabuleiro)
            else:
                print("Não conseguiu conectar.")
                return False
            
            print("Conseguiu conectar!")
            return self.___pedras.pop(indice_minha_pedra)


# === COISAS PARA TESTES ABAIXO === #

meu_jogo = Jogo()

meu_jogador = meu_jogo.jogador_principal

def exibir_lista_pedras(minhas_pedras):
    for i, pedra in enumerate(minhas_pedras):
        print(f"--[ PEDRA {i} ]--")
        print(pedra.valor_0, " /", pedra.valor_1, "\n")

    print(f"--[TABULEIRO]--")
    tabuleiro_para_print = []

    for p in meu_jogo.tabuleiro:
        tabuleiro_para_print.append(str(p))

    print(tabuleiro_para_print)

# LOOP PARA FINS DE TESTE.
# MUDE PARA True CASO QUEIRA TESTAR.
while False:

    print("PEDRAS IA: ")
    exibir_lista_pedras(meu_jogo.jogador_IA.get_pedras())

    print("\n -> MINHAS PEDRAS: ")
    exibir_lista_pedras(meu_jogador.get_pedras())

    pedra_conectar_0 = int(input("Digite o indice da sua pedra para conectar: "))

    pedra_conectar_1 = int(input("Digite a extremidade da pedra do tabuleiro para conectar (0 ou -1): "))
    outra_pedra = meu_jogo.tabuleiro[pedra_conectar_1]

    meu_jogador.inserir_pedra(pedra_conectar_0, outra_pedra, pedra_conectar_1)

    print("VEZ DA IA:\n")

    meu_jogo.jogador_IA.jogada_ia()

    time.sleep(0.6)


