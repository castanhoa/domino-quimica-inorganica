import Domino
import random
import copy
import time

quantia_total_pedras = 28

def sub_lists(l0:list, l1:list):
    return list( set(l0) - set(l1) )

def conversor_extremidade_to_cima(extremidade:int):
    return True if extremidade >= 0 else False

def obter_identidade_pedra(pedra):
    identidade = [

        Domino.obter_funcao_elemento(pedra.valor_0),

        Domino.obter_funcao_elemento(pedra.valor_1),

    ]

    return identidade

def obter_rotulo_pedra(pedra):
    rotulo = [
        pedra.valor_0,

        pedra.valor_1,
    ]

    return rotulo

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

    #local_pedra_b = tabuleiro.index(pedra_b)

    if conectar_acima == False:
        tabuleiro.append(pedra_a)
    else:
        tabuleiro.insert(0, pedra_a)

class Jogo:
    def __init__(self, objAluno):
        
        self.objAluno = objAluno

        self.difficuldade = objAluno.obter_dificuldade()

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


        self.jogador_IA = self.Jogador(jogo=self, apelido="Bot")
        jog_ia_pedras = random.sample(todas_pedras, quantia_total_pedras // 4)
        self.jogador_IA.inicializar_pedras(jog_ia_pedras)
        todas_pedras = sub_lists(todas_pedras, self.jogador_IA.get_pedras())

    def resultado(self):

        jogo_trancado = True
        jogo_finalizado = False

        if len(self.monte) == 0:
            # ver se a ia esta trancada
            for pedra in self.jogador_IA.get_pedras():
                if Domino.deep_e_compativel(pedra, self.tabuleiro[0]) or Domino.deep_e_compativel(pedra, self.tabuleiro[-1]):
                    jogo_trancado = False
                    break
            
            # ver se o usuario esta trancado
            for pedra in self.jogador_principal.get_pedras():
                if Domino.deep_e_compativel(pedra, self.tabuleiro[0]) or Domino.deep_e_compativel(pedra, self.tabuleiro[-1]):
                    jogo_trancado = False
                    break
        else:
            jogo_trancado = False

        aluno_venceu = True
        
        if jogo_trancado == True:
            aluno_venceu = len(self.jogador_principal.get_pedras()) >= len(self.jogador_IA.get_pedras())
            jogo_finalizado = True
                # usuario venceu

        if len(self.jogador_IA.get_pedras()) == 0:
            jogo_finalizado = True
            aluno_venceu = False

        if len(self.jogador_principal.get_pedras()) == 0:
            jogo_finalizado = True
            aluno_venceu = True

        if jogo_finalizado != True:
            return False

        tentativas_conexao, tentativas_conexao_erradas = self.jogador_principal.get_tentativas_conexao()

        len_tentativas_conexao = len(tentativas_conexao)
        len_tentativas_conexao_certas = len_tentativas_conexao - len(tentativas_conexao_erradas)

        # atualizar dados do aluno
        self.objAluno.resultado(aluno_venceu, len_tentativas_conexao, len_tentativas_conexao_certas)

        return True

    class Jogador:
        def __init__(self, jogo:Jogo, apelido):
            self.jogo = jogo
            self.__pedras = []
            self.__apelido = apelido
            self.__tentativas_conexao = []
            self.__tentativas_erradas_conexao = []
        
        def inicializar_pedras(self, minhas_pedras:list):
            if len(self.__pedras) == 0:
                self.__pedras = minhas_pedras

        def get_pedras(self):
            return copy.copy(self.__pedras)
        
        def jogada_ia(self):
            tabuleiro = self.jogo.tabuleiro

            chance_erro = min(1, max(0.5, 1-self.jogo.difficuldade))

            pedra_extremidade_0 = tabuleiro[0]
            pedra_extremidade_1 = tabuleiro[-1]

            possiveis_jogadas = []
            
            for indice_minha_pedra, minha_pedra in enumerate(self.__pedras):
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

            num_jogadas_erradas = int((len(possiveis_jogadas) - 1)*chance_erro / (1 - chance_erro))

            for _ in range(num_jogadas_erradas):
                possivel_jogada = {
                        'indice_minha_pedra': random.randint(0, len(self.__pedras) - 1), 
                        'pedra_alvo': self.jogo.tabuleiro[random.randint(-1,0)],
                        'cima': True if random.randint(0,1) == 1 else False,
                        }
                possiveis_jogadas.append(possivel_jogada)            

            if len(possiveis_jogadas) > 0:
                jogada_escolhida = random.choice(possiveis_jogadas)

                indice_minha_pedra = jogada_escolhida['indice_minha_pedra']
                pedra_conexao = jogada_escolhida['pedra_alvo']
                cima = jogada_escolhida['cima']
                 
                sucesso = self.inserir_pedra(indice_minha_pedra=indice_minha_pedra, pedra_conexao=pedra_conexao, extremidade=(cima))

                if sucesso != False and len(self.__pedras) > 0:
                    print("IA Conseguiu conectar!")
                    self.__pedras.pop(indice_minha_pedra)

                    return True
                else:
                    return False
                
            else:
                
                self.comprar_pedra()

                return False

        def comprar_pedra(self):
            if len(self.jogo.monte) > 0:
                nova_pedra = (self.jogo.monte.pop(-1))
                self.__pedras.append(nova_pedra)

                print(f"JOGADOR {self.__apelido} COMPROU PEDRA {nova_pedra}")
                
            else:
                print(f"JOGADOR {self.__apelido} TENTOU COMPRAR PEDRA, MAS NAO HA MAIS PEDRAS NO MONTE")

        def inserir_pedra(self, indice_minha_pedra, pedra_conexao, extremidade:int):

            print("=== TENTATIVA INSERIR PEDRA ===")
            
            tabuleiro = self.jogo.tabuleiro

            extremidade = 0 if extremidade >= 0 else -1

            cima = extremidade == 0

            minha_pedra = self.__pedras[indice_minha_pedra]

            dupla = minha_pedra.valor_0 == minha_pedra.valor_1

            # eita codigo ineficiente. devera ser melhorado.
                       
            tentativa_conexao = {
                'minha_pedra': minha_pedra, 
                'pedra_alvo': pedra_conexao,
                'indice': len(self.jogo.tabuleiro)
            }

            self.__tentativas_conexao.append(tentativa_conexao)

            sucesso = False

            if (pedra_conexao.valor_0_conexao == None):
                if Domino.e_compativel(minha_pedra.valor_0, pedra_conexao.valor_0) == True:
                    sucesso = conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=True, pedra_b=pedra_conexao, pedra_b_valor_0=True, conectar_acima=cima, tabuleiro=tabuleiro)

                    if dupla == True:
                        conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=False, pedra_b=pedra_conexao, pedra_b_valor_0=True, conectar_acima=cima, tabuleiro=tabuleiro)  
                
                elif Domino.e_compativel(minha_pedra.valor_1, pedra_conexao.valor_0) == True:
                    sucesso = conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=False, pedra_b=pedra_conexao, pedra_b_valor_0=True, conectar_acima=cima, tabuleiro=tabuleiro)

                    if dupla == True:
                        conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=True, pedra_b=pedra_conexao, pedra_b_valor_0=True, conectar_acima=cima, tabuleiro=tabuleiro)

            elif (pedra_conexao.valor_1_conexao == None):
                if Domino.e_compativel(minha_pedra.valor_0, pedra_conexao.valor_1) == True:
                    sucesso = conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=True, pedra_b=pedra_conexao, pedra_b_valor_0=False, conectar_acima=cima, tabuleiro=tabuleiro)

                    if dupla == True:
                        conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=True, pedra_b=pedra_conexao, pedra_b_valor_0=False, conectar_acima=cima, tabuleiro=tabuleiro)
                
                elif Domino.e_compativel(minha_pedra.valor_1, pedra_conexao.valor_1) == True:
                    sucesso = conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=False, pedra_b=pedra_conexao, pedra_b_valor_0=False, conectar_acima=cima, tabuleiro=tabuleiro)

                    if dupla == True:
                        conectar_pedras (pedra_a=minha_pedra, pedra_a_valor_0=True, pedra_b=pedra_conexao, pedra_b_valor_0=False, conectar_acima=cima, tabuleiro=tabuleiro)

            if sucesso == False:
                self.__tentativas_erradas_conexao.append(tentativa_conexao)
               
                print("Não conseguiu conectar.")
                return False
            
            print("PLAYER Conseguiu conectar!")
            return self.__pedras.pop(indice_minha_pedra)

        def get_tentativas_conexao(self):
            return self.__tentativas_conexao, self.__tentativas_erradas_conexao
        
        def get_correcoes_dos_erros(self, retornar_string:bool):
            tentativas_totais, tentativas_erradas = self.get_tentativas_conexao()

            correcoes = []

            for tentativa in tentativas_erradas:
                minha_pedra = tentativa["minha_pedra"]
                pedra_alvo = tentativa["pedra_alvo"]
                
                correcao_minha_pedra = obter_identidade_pedra(minha_pedra)
                correcao_pedra_alvo = obter_identidade_pedra(pedra_alvo)

                correcoes.append([correcao_minha_pedra, correcao_pedra_alvo])

            if retornar_string == True:
                correcoes

            else:
                s = ""

                for i, tentativa in enumerate(correcoes):

                    minha_pedra_rotulo = obter_rotulo_pedra(tentativas_erradas[i]["minha_pedra"])

                    pedra_conexao_rotulo = obter_rotulo_pedra(tentativas_erradas[i]["pedra_alvo"])

                    s += f"======================================================\n"
                    s += f"=== {i+1}º tentativa incorreta de {self.__apelido} ===\n"
                    s += f" - Peça que tentou jogar: {minha_pedra_rotulo}\n"
                    s += f"  `--> Suas funções: {tentativa[0]}\n\n"

                    s += f" - Peça que tentou conectar a: {pedra_conexao_rotulo}\n"
                    s += f"  `--> Suas funções: {tentativa[1]}\n"

                return s, len(tentativas_erradas) / max(1, len(tentativas_totais))



# # === COISAS PARA TESTES ABAIXO === #

# meu_jogo = Jogo()

# meu_jogador = meu_jogo.jogador_principal

# def exibir_lista_pedras(minhas_pedras):
#     for i, pedra in enumerate(minhas_pedras):
#         print(f"--[ PEDRA {i} ]--")
#         print(pedra.valor_0, " /", pedra.valor_1, "\n")

#     print(f"--[TABULEIRO]--")
#     tabuleiro_para_print = []

#     for p in meu_jogo.tabuleiro:
#         tabuleiro_para_print.append(str(p))

#     print(tabuleiro_para_print)

# # LOOP PARA FINS DE TESTE.
# # MUDE PARA True CASO QUEIRA TESTAR.
# while False:

#     print("PEDRAS IA: ")
#     exibir_lista_pedras(meu_jogo.jogador_IA.get_pedras())

#     print("\n -> MINHAS PEDRAS: ")
#     exibir_lista_pedras(meu_jogador.get_pedras())

#     pedra_conectar_0 = int(input("Digite o indice da sua pedra para conectar: "))

#     pedra_conectar_1 = int(input("Digite a extremidade da pedra do tabuleiro para conectar (0 ou -1): "))
#     outra_pedra = meu_jogo.tabuleiro[pedra_conectar_1]

#     meu_jogador.inserir_pedra(pedra_conectar_0, outra_pedra, pedra_conectar_1)

#     print("VEZ DA IA:\n")

#     meu_jogo.jogador_IA.jogada_ia()

#     time.sleep(0.6)


