from limite.tela_transporte import TelaTransporte
from entidade.transporte import Transporte
from entidade.empresa import Empresa


class ControladorTransportes():
    def __init__(self, controlador_sistema):
        self.__tela_transporte = TelaTransporte(self)
        self.__controlador_sistema = controlador_sistema
        self.__transportes = []
    
    @property
    def transportes(self):
        return self.__transportes
    
    def find_transporte(self, tipo: str):
        for transporte in self.__transportes:
            if transporte.tipo == tipo:
                return transporte
        return None
    
    def incluir_transporte(self):
        dados_transporte = self.__tela_transporte.pega_dados_transporte()
        if dados_transporte is None: 
            return None
        transporte = self.find_transporte(dados_transporte['tipo'])
        if transporte is not None:
            self.__tela_transporte.mostra_mensagem('Erro: esse transporte já foi criado.')
            return None
        novo_transporte = Transporte(dados_transporte['tipo'])
        self.__transportes.append(novo_transporte)
        self.__tela_transporte.mostra_mensagem('Transporte incluído com sucesso!')
    
    def excluir_transporte(self):
        self.listar_transportes()
        if not self.__transportes:
            return

        dados_selecao = self.__tela_transporte.seleciona_transporte()
        if dados_selecao is None:
            self.__tela_transporte.mostra_mensagem("Exclusão cancelada.")
            return    
        transporte_a_remover = self.find_transporte(dados_selecao['tipo'])
        if transporte_a_remover is not None:
            self.__transportes.remove(transporte_a_remover)
            self.__tela_transporte.mostra_mensagem('Transporte removido com sucesso!')
        else:
            self.__tela_transporte.mostra_mensagem(
                f'Erro: O transporte NÃO está cadastrado!'
            )
    
    def alterar_transporte(self):
        self.listar_transportes()
        if not self.__transportes:
            return

        dados_identificacao = self.__tela_transporte.seleciona_transporte()
        if dados_identificacao is None:
            self.__tela_transporte.mostra_mensagem("Alteração cancelada.")
            return
        transporte_a_alterar = self.find_transporte(dados_identificacao['tipo'])
        if transporte_a_alterar is not None:
            novos_dados = self.__tela_transporte.pega_dados_transporte()
            transporte_a_alterar.tipo = novos_dados['tipo']
            self.listar_transportes()
        else:
            self.__tela_transporte.mostra_mensagem('Erro: Transporte não encontrado.')
    
    def listar_transportes(self):
        self.__tela_transporte.mostra_mensagem("--- Lista de Transportes Registrados ---")
        if not self.__transportes:
            self.__tela_transporte.mostra_mensagem("Nenhum transporte registrado.")
            return
        for transporte in self.__transportes:
            self.__tela_transporte.mostra_transportes(transporte)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_transporte,
            2: self.excluir_transporte,
            3: self.alterar_transporte,
            4: self.listar_transportes
        }
        while True:
            opcao = self.__tela_transporte.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
    
