from TelaCarregamento import TelaCarregamento
from TelaEstatisticas import TelaEstatisticas
from TelaRegras import TelaRegras
from TelaRelatorio import TelaRelatorio
from TelaInicial import TelaInicial
from TelaDeJogo import TelaDeJogo
from TelaLogin import TelaLogin
import pygame

TELAS = {
    "login": TelaLogin,
    "inicio": TelaInicial,
    "jogo": TelaDeJogo,
    "estatisticas": TelaEstatisticas,
    "relatorio": TelaRelatorio,
    "regras": TelaRegras
}

def main():
    pygame.init()
    tela_atual = TelaLogin()

    while tela_atual:
        tela_atual.executar()
        proxima = tela_atual.proxima_tela
        
        if proxima is None:
            break

        TelaCarregamento.mostrar_loading()
        tela_atual = TELAS[proxima]()

    pygame.quit()

if __name__ == "__main__":
    main()
