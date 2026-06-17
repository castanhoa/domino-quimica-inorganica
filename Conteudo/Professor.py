from Conteudo.Usuario import Usuario

class Professor(Usuario):
    def __init__(self, senha:str , nome:str , logado_ao_criar_conta:bool=False):
        super().__init__(senha, nome, logado_ao_criar_conta)
