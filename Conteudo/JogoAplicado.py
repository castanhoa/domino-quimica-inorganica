from EstruturaJogo import Jogo
from TelaDeJogo import TelaDeJogo
from Peca import Peca
import random

# import Imagens.CaminhosImagens as imgs_paths

import time
from Aluno import Aluno

meu_aluno = Aluno("123", "Robert", 1, True)

# vez do jogador é quando:
# (self.rodada + self.rodada_offset) % 2 == 0

class Jogatina:
    def __init__(self, objAluno):
        self.jogo = Jogo(objAluno=objAluno)
    
        self.tela = TelaDeJogo(objJogatina=self)

        self.rodada = 0
        self.rodada_antiga = -1

        self.rodada_offset = random.randint(0,1)
        self.jogo_finalizado = False

        self.tempo_inicio_partida = -1
        self.tempo_fim_partida = -1

    def get_vez(self):
        return (self.rodada + self.rodada_offset) % 2

        # if vez == 0:
        #     return vez, self.jogo.jogador_principal, self.tela.mao
        # else:
        #     return vez, self.jogo.jogador_IA, self.tela.mao_bot

    def converter_pedra_back_para_front(self, objPedra, posicao, is_player:bool):
        id_pedra = str(hash(objPedra))

        x = self.tela.largura // 2 - int(275 * self.tela.escala) + int(80 * self.tela.escala) * posicao
        y = self.tela.altura // 2 + int(220 * self.tela.escala)

        self.tela.registrar_rect(id_pedra, x, y, 70, 140)

        rect = getattr(self.tela, id_pedra)

        rect.width = self.tela.tamanho_peca_player[0]
        rect.height = self.tela.tamanho_peca_player[1]

        frontPeca = Peca(imagem=(self.tela.pecaPlayer if is_player else self.tela.pecaBot), rect=rect, referenciaBackend=objPedra )

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

        print(f"LEN(TABULEIRO) = {len(self.jogo.tabuleiro)}")
        print(f"LEN(MESA) = {len(self.tela.mesa.pecas)}")


    def get_jogada(self, minha_mao, peca_front_conectar, extremidade:int):
        if peca_front_conectar not in minha_mao.pecas:
            print("ERRO! NAO PODE POIS VOCE NAO TEM ESSA PECA")
            return

        minha_peca_index = minha_mao.pecas.index(peca_front_conectar)
        outra_peca = self.tela.mesa.pecas[extremidade]

        return (minha_peca_index, outra_peca.referenciaBackend, extremidade)
    
    def fazer_jogada_usuario(self, peca_front_conectar):

        if self.get_vez() != 0:
            print("Não é a vez do usuário, e sim do bot.")
            return

        minha_mao = self.tela.mao

        jogadas = [
            self.get_jogada(minha_mao, peca_front_conectar, 0),
            self.get_jogada(minha_mao, peca_front_conectar, -1)
        ]
        
        self.rodada += 1

        for pot_jogada in jogadas:
            jogada = self.jogo.jogador_principal.inserir_pedra(*pot_jogada)

            if jogada != False:
                break
        
        self.atualizar_pedras_ui()

        self.rodada_antiga = self.rodada


    def realizar_rodada(self):

        if self.jogo_finalizado:
            print("JOGO FINALIZADO")
            return True

        self.atualizar_pedras_ui()
        self.jogo_finalizado = self.jogo.resultado(self.tempo_fim_partida-self.tempo_inicio_partida)
        if self.jogo_finalizado:
            print("JOGO FINALIZADO")
            return True
        
        self.tempo_fim_partida = time.perf_counter()
        print(f"VEZ: {self.get_vez()}")
            
        if self.get_vez() == 1:
            self.jogo.jogador_IA.jogada_ia()

            self.rodada_antiga = self.rodada
            self.rodada += 1

    def iniciar_partida(self):
        self.tempo_inicio_partida = time.perf_counter()
        self.tela.executar(self.realizar_rodada)


minha_jogatina = Jogatina(meu_aluno)
minha_jogatina.iniciar_partida()

        # for i in range(7):
        #     nome = f"botao_peca_{i}"
        #     self.registrar_rect(nome, x, y, 70, 140)
        #     x += int(80 * self.tela.escala)

        # for i in range(7):
        #     rect = getattr(self, f"botao_peca_{i}")
        #     rect.width = self.tamanho_peca_player[0]
        #     rect.height = self.tamanho_peca_player[1]
        #     peca = Peca(self.pecaPlayer, rect)
        #     self.mao.adicionar(peca)

        # for i in range(7):
        #     rect = pygame.Rect(x, y, 50, 100)
        #     peca = Peca(self.pecaBot, rect)
        #     self.mao_bot.adicionar(peca)
        #     x += int(60 * self.escala)


    