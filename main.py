from Conteudo.TelaCarregamento import TelaCarregamento
from Conteudo.TelaEstatisticas import TelaEstatisticas
from Conteudo.TelaRegras import TelaRegras
from Conteudo.TelaRelatorio import TelaRelatorio
from Conteudo.TelaInicial import TelaInicial
from Conteudo.TelaDeJogo import TelaDeJogo
from Conteudo.TelaLogin import TelaLogin

from Conteudo.UsuarioSentinela import UsuarioSentinela

from Conteudo.Banco import atualizar
from Conteudo.Aluno import Aluno

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

    minha_casca_usuario = UsuarioSentinela()

    tela_atual = TelaLogin(minha_casca_usuario)

    while tela_atual:

        if isinstance(minha_casca_usuario.objUsuario, Aluno):
            atualizar(minha_casca_usuario.objUsuario) 

        metodo_adicional = None

        if hasattr(tela_atual, "objJogatina"):
            metodo_adicional = tela_atual.objJogatina.realizar_rodada

        tela_atual.executar(metodo_adicional)
        proxima = tela_atual.proxima_tela
        
        if proxima is None:
            break
        
        TelaCarregamento.mostrar_loading()
        tela_atual = TELAS[proxima](minha_casca_usuario.objUsuario)

    pygame.quit()

if __name__ == "__main__":
    main()
