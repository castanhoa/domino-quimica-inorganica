from Conteudo.EstruturaJogo import Jogo
from Conteudo.Peca import Peca
import random

# import Imagens.CaminhosImagens as imgs_paths

import time
import threading

# vez do jogador é quando:
# (self.rodada + self.rodada_offset) % 2 == 0

class ClasseRodada:
    def __init__(self, offset:int):
        self.__rodada = offset

    def incrementar(self):
        self.__rodada += 1

    def get_vez(self):
        return (self.__rodada) % 2


class Jogatina:
    def __init__(self, objAluno, tela_de_jogo):
        self.jogo = Jogo(objAluno=objAluno)
    
        self.tela = tela_de_jogo
        
        # rodada_offset = random.randint(0,1)
        self.rodada = ClasseRodada(offset=random.randint(0,1))

        self.jogo_finalizado = False

        self.tempo_inicio_partida = -1
        self.tempo_fim_partida = -1


    def converter_pedra_back_para_front(self, objPedra, posicao, is_player:bool):
        id_pedra = str(hash(objPedra))

        x = self.tela.largura // 2 - int(275 * self.tela.escala) + int(80 * self.tela.escala) * posicao
        y = self.tela.altura // 2 + int(220 * self.tela.escala)

        self.tela.registrar_rect(id_pedra, x, y, 70, 140)

        rect = getattr(self.tela, id_pedra)

        rect.width = self.tela.tamanho_peca_player[0]
        rect.height = self.tela.tamanho_peca_player[1]

        frontPeca = Peca(imagem=(self.tela.pecaPlayer if is_player else self.tela.pecaBot), rect=rect, referenciaBackend=objPedra, publica=is_player)

        return frontPeca

    def atualizar_pedras_ui(self):

        for i, pedra in enumerate(self.jogo.jogador_principal.get_pedras()):
            ui_peca = self.converter_pedra_back_para_front(pedra, i, True)

            if ui_peca not in self.tela.mao.pecas:
                self.tela.mao.adicionar(ui_peca)
        
        for peca in self.tela.mao.pecas:
            if peca.referenciaBackend not in self.jogo.jogador_principal.get_pedras():
                self.tela.mao.remover(peca)

        #-------------#

        for i, pedra in enumerate(self.jogo.jogador_IA.get_pedras()):
            ui_peca = self.converter_pedra_back_para_front(pedra, i, False)

            if ui_peca not in self.tela.mao_bot.pecas:
                self.tela.mao_bot.adicionar(ui_peca)
        
        for peca in self.tela.mao_bot.pecas:
            if peca.referenciaBackend not in self.jogo.jogador_IA.get_pedras():
                self.tela.mao_bot.remover(peca)

        #-------------#

        for i, pedra in enumerate(self.jogo.tabuleiro):
            ui_peca = self.converter_pedra_back_para_front(pedra, i, True)

            if ui_peca not in self.tela.mesa.pecas:
                self.tela.mesa.adicionar_peca(ui_peca, (0 if i == 0 else -1))

        #print(f"LEN(TABULEIRO) = {len(self.jogo.tabuleiro)}")
        #print(f"LEN(MESA) = {len(self.tela.mesa.pecas)}")


    def get_jogada(self, minha_mao, peca_front_conectar, extremidade:int):
        if peca_front_conectar not in minha_mao.pecas:
            print("ERRO! NAO PODE POIS VOCE NAO TEM ESSA PECA")
            return

        minha_peca_index = minha_mao.pecas.index(peca_front_conectar)
        outra_peca = self.tela.mesa.pecas[extremidade]

        return (minha_peca_index, outra_peca.referenciaBackend, extremidade)
    
    def fazer_jogada_usuario(self, peca_front_conectar):

        if self.rodada.get_vez() != 0:
            print("Não é a vez do usuário, e sim do bot.")
            return

        minha_mao = self.tela.mao

        jogadas = [
            self.get_jogada(minha_mao, peca_front_conectar, 0),
            self.get_jogada(minha_mao, peca_front_conectar, -1)
        ]
        
        self.rodada.incrementar()

        for pot_jogada in jogadas:
            jogada = self.jogo.jogador_principal.inserir_pedra(*pot_jogada)

            if jogada != False:
                break
        
        self.atualizar_pedras_ui()


    def comprar_peca_usuario(self):
        if self.rodada.get_vez() != 0:
            print("Não é a vez do usuário, e sim do bot.")
            return
        
        self.rodada.incrementar()

        self.jogo.jogador_principal.comprar_pedra()
        
        self.atualizar_pedras_ui()


    def realizar_rodada(self):

        if self.jogo_finalizado:
            print("JOGO FINALIZADO")
            self.tela.proxima_tela = "fim_de_jogo"
            return True
        
        if self.rodada.get_vez() == 0:
            self.tela.mudar_turno("jogador")
        else:
            self.tela.mudar_turno("bot")

        self.atualizar_pedras_ui()
        self.jogo_finalizado, _, _ = self.jogo.resultado(self.tempo_fim_partida-self.tempo_inicio_partida)
        if self.jogo_finalizado:
            print("JOGO FINALIZADO")
            return True
        
        self.tempo_fim_partida = time.perf_counter()
        #print(f"VEZ: {self.rodada.get_vez()}")
            
        if self.rodada.get_vez() == 1:
            threading.Thread(target=self.jogo.jogador_IA.jogada_ia, args=[self.rodada]).start()


    def iniciar_partida(self):
        self.tempo_inicio_partida = time.perf_counter()
