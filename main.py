from Conteudo.TelaCarregamento import TelaCarregamento
from Conteudo.TelaEstatisticas import TelaEstatisticas
from Conteudo.TelaRegras import TelaRegras
from Conteudo.TelaRelatorio import TelaRelatorio
from Conteudo.TelaInicial import TelaInicial
from Conteudo.TelaDeJogo import TelaDeJogo
from Conteudo.TelaLogin import TelaLogin
from Conteudo.TelaComandos import TelaComandos
from Conteudo.TelaFimDeJogo import TelaFimDeJogo

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
    "regras": TelaRegras,
    "comandos": TelaComandos,
    "fim_de_jogo": TelaFimDeJogo,
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
        
        booleano_adicional = None
        string_adicional = None

        if not tela_atual.recado_final is None and isinstance(tela_atual, TelaDeJogo):
            _, booleano_adicional, string_adicional = tela_atual.recado_final

        TelaCarregamento.mostrar_loading()
        classe_tela_atual = TELAS[proxima]
        if (classe_tela_atual is TelaFimDeJogo):
            tela_atual = classe_tela_atual(minha_casca_usuario.objUsuario, booleano_adicional, string_adicional)
        
        else:
            tela_atual = classe_tela_atual(minha_casca_usuario.objUsuario)


    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
