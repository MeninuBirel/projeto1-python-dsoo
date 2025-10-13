from limite.tela_transporte import TelaTransporte
from entidade.transporte import Transporte
from entidade.empresa import Empresa

class ControladorTransporte():
    def __init__(self, controlador_sistema):
        self.__tela_transporte = TelaTransporte(self)
        self.__controlador_sistema = controlador_sistema
        self.__transportes = []
    
    @property
    def transportes(self):
        return self.__transportes
    
    @property
    def controlador_empresas(self):
        return self.__controlador_sistema.controlador_empresas
    
    def find_transporte(self, tipo: str, empresa: Empresa):
        for transporte in self.__transportes:
            if transporte.tipo == tipo and transporte.empresa == empresa:
                return transporte
        return None
    
    def incluir_transporte(self):
        dados_transporte = self.__tela_transporte.pega_dados_transporte()
        if dados_transporte is None: # Se a seleção de empresa foi cancelada
            return None
            
        empresa_obj = dados_transporte['empresa'] # Objeto Empresa
        transporte = self.find_transporte(dados_transporte['tipo'], empresa_obj)
        if transporte is not None:
            self.__tela_transporte.mostra_mensagem('Erro: esse transporte já foi criado.')
            return None
        novo_transporte = Transporte(dados_transporte['tipo'], empresa_obj)
        self.__transportes.append(novo_transporte)
        self.__tela_transporte.mostra_mensagem('Transporte incluído com sucesso!')


    def excluir_transporte(self):
        self.lista_transportes()
        if not self.__transportes:
            return # Já tratado em listar_trasnportes, mas por segurança.

        # Pede os dados para identificar o transporte a ser excluído
        dados_selecao = self.__tela_transporte.seleciona_transporte()
        if dados_selecao is None:
            self.__tela_transporte.mostra_mensagem("Exclusão cancelada.")
            return

        # Busca o objeto Empresa usando o CNPJ fornecido
        empresa_selecionada = self.controlador_empresas.find_empresa_by_cnpj(dados_selecao['cnpj'])
        if empresa_selecionada is None:
             self.__tela_transporte.mostra_mensagem('Erro: Empresa não encontrada para o CNPJ fornecido.')
             return
        # Busca o objeto Transporte pela combinação tipo e Empresa
        transporte_a_remover = self.find_transporte(dados_selecao['tipo'], empresa_selecionada)
        if transporte_a_remover is not None:
            self.__transportes.remove(transporte_a_remover)
            self.__tela_transporte.mostra_mensagem('Transporte removido com sucesso!')
        else:
            self.__tela_transporte.mostra_mensagem(
                f'Erro: O transporte Tipo "{dados_selecao["tipo"]}" com a empresa "{empresa_selecionada.nome}" NÃO está cadastrado!'
            )
        
    def alterar_transporte(self):
        self.lista_transportes()
        if not self.__transportes:
            return

        # 1. Pede os dados para IDENTIFICAR o transporte a ser alterado
        dados_identificacao = self.__tela_transporte.seleciona_transporte()
        if dados_identificacao is None:
            self.__tela_transporte.mostra_mensagem("Alteração cancelada.")
            return

        empresa = self.controlador_empresas.find_empresa_by_cnpj(dados_identificacao['cnpj'])
        if empresa is None:
             self.__tela_transporte.mostra_mensagem('Erro: Empresa não encontrada para o CNPJ fornecido.')
             return

        # 1.2. Busca o Transporte
        transporte_a_alterar = self.find_transporte(dados_identificacao['tipo'], empresa)
        if transporte_a_alterar is not None:
            novos_dados = self.__tela_transporte.pega_dados_transporte()
            transporte_a_alterar.tipo = novos_dados['tipo']
            transporte_a_alterar.empresa = novos_dados['empresa']
            self.lista_transportes()
        else:
            self.__tela_transporte.mostra_mensagem('Erro: Transporte não encontrado.')

    
    def lista_transportes(self):
        for transporte in self.__transportes:
            self.__tela_transporte.mostra_transporte({
                'tipo': transporte.tipo,
                'empresa': transporte.empresa,
            })
            
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
