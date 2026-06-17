from Conteudo.Seguranca.AjudaHash import hash_padrao, comparar_hashes


class Usuario():
    # init seria para cadastrar o usuario generico
    def __init__(self, senha:str , nome:str , logado_ao_criar_conta:bool=False):
        self.__hash_senha_fatual = hash_padrao(senha)
        self.__nome_fatual= nome
        self.__logado = logado_ao_criar_conta

    def get_username(self):
        return self.__nome_fatual

    def tentar_login(self, senha, nome):
        if ( self.__nome_fatual == nome ) and ( comparar_hashes(self.__hash_senha_fatual , hash_padrao(senha)) ):
            self.__logado = True
            return self.__logado

        self.__logado = False
        return self.__logado

    def deslogar(self):
        self.__logado = False
        return self.__logado

