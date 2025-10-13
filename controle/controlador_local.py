from entidade.local import Local
from limite.tela_local import TelaLocal


class ControladorLocais():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__locais = []
        self.__tela_local = TelaLocal(self)

    @property
    def locais(self):
        return self.__locais

    def find_local_by_cidade(self, cidade: str):
        for local in self.__locais:
            if local.cidade == cidade:
                return local
        return None

    def incluir_local(self):
        dados_local = self.__tela_local.pega_dados_local()
        cidade = dados_local['cidade']
        local = self.find_local_by_cidade(cidade)
        if local is None:
            novo_local = Local(dados_local['cidade'], dados_local['pais'])
            self.__locais.append(novo_local)
            self.__tela_local.mostra_mensagem("Local cadastrado com sucesso!")
        else:
            self.__tela_local.mostra_mensagem("Erro: Esse local já está cadastrado!")
        return None

    def excluir_local(self):
        self.lista_locais()
        cidade = self.__tela_local.seleciona_local()
        local_a_remover = self.find_local_by_cidade(cidade)
        if local_a_remover is not None:
            self.__locais.remove(local_a_remover)
            self.__tela_local.mostra_mensagem('Local removido com sucesso!')
        else:
            self.__tela_local.mostra_mensagem(f'Erro: esse local NÃO está cadastrado!')
    
    def alterar_local(self):
        self.lista_locais()
        identificacao_local = self.__tela_local.seleciona_local()
        local = self.find_local_by_cidade(identificacao_local)
        if local is not None:
            novos_dados = self.__tela_local.pega_dados_local()
            local.cidade = novos_dados['cidade']
            local.pais = novos_dados['pais']
            self.lista_locais()
        else:
            self.__tela_local.mostra_mensagem('Erro: local não está cadastrado')

    
    def listar_locais(self):
        self.__tela_local.mostra_mensagem("--- Lista de Locais Registrados ---")
        if not self.__locais:
            self.__tela_local.mostra_mensagem("Nenhum local registrado.")
            return
        for local in self.__locais:
            self.__tela_local.mostra_locais(local)

    def lista_locais(self):
        for local in self.__locais:
            self.__tela_local.mostra_local({
                'cidade': local.cidade,
                'pais': local.pais
            })

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_local,
            2: self.excluir_local,
            3: self.alterar_local,
            4: self.listar_locais
        }
        while True:
            opcao = self.__tela_local.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
