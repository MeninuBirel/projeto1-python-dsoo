from entidade.trecho import Trecho
from limite.tela_trecho import TelaTrecho
from entidade.local import Local
from entidade.transporte import Transporte
from collections import defaultdict


class ControladorTrechos():
    def __init__(self, controlador_sistema):
        self.__tela_trecho = TelaTrecho(self)
        self.__trechos = []
        self.__controlador_sistema = controlador_sistema

    @property
    def trechos(self):
        return self.__trechos

    @property
    def controlador_transportes(self):
        return self.__controlador_sistema.controlador_transportes
    
    @property
    def controlador_locais(self):
        return self.__controlador_sistema.controlador_locais
    
    def find_trecho(self, data: str, origem: Local, destino: Local, transporte: Transporte):
        for trecho in self.__trechos:
            if trecho.data == data and trecho.origem == origem and trecho.destino == destino and trecho.transporte == transporte:
                return trecho
        return None
    
    def incluir_trecho(self):
        dados_trecho = self.__tela_trecho.pega_dados_trecho()
        if dados_trecho is None: 
            return None
            
        origem_obj = dados_trecho['origem'] # Objeto origem
        destino_obj = dados_trecho['destino']
        transporte_obj = dados_trecho['transporte']
        trecho = self.find_trecho(dados_trecho['data'], origem_obj, destino_obj, transporte_obj)
        if trecho is not None:
            self.__tela_trecho.mostra_mensagem('Erro: esse trecho já foi criado.')
            return None
        novo_trecho = Trecho(dados_trecho['data'], origem_obj, destino_obj, transporte_obj, dados_trecho['valor_trecho'])
        self.__trechos.append(novo_trecho)
        self.__tela_trecho.mostra_mensagem('Trecho incluído com sucesso!')

    def excluir_trecho(self):
        self.listar_trechos()
        if not self.__trechos:
            return

        # Pede os dados para identificar o trecho a ser excluído
        self.__tela_trecho.mostra_mensagem("\n--- Selecione o Trecho a ser Excluído ---")
        dados_selecao = self.__tela_trecho.pega_dados_trecho() 
        
        if dados_selecao is None:
            self.__tela_trecho.mostra_mensagem("Exclusão cancelada.")
            return

        # Busca o objeto Trecho
        trecho_a_remover = self.find_trecho(
            dados_selecao['data'],
            dados_selecao['origem'],
            dados_selecao['destino'],
            dados_selecao['transporte']
        )
        
        if trecho_a_remover is not None:
            self.__trechos.remove(trecho_a_remover)
            self.__tela_trecho.mostra_mensagem('Trecho removido com sucesso!')
        else:
            self.__tela_trecho.mostra_mensagem('Erro: O trecho com os dados informados NÃO está cadastrado!')
    
    def alterar_trecho(self):
        self.listar_trechos()
        if not self.__trechos:
            return

        # 1. Pede os dados para IDENTIFICAR o trecho a ser alterado (os dados ATUAIS)
        self.__tela_trecho.mostra_mensagem("\n--- Identifique o Trecho a ser Alterado (Dados Atuais) ---")
        dados_identificacao = self.__tela_trecho.pega_dados_trecho()
        
        if dados_identificacao is None:
            self.__tela_trecho.mostra_mensagem("Alteração cancelada.")
            return

        # 1.2. Busca o Trecho
        trecho_a_alterar = self.find_trecho(
            dados_identificacao['data'],
            dados_identificacao['origem'],
            dados_identificacao['destino'],
            dados_identificacao['transporte']
        )
        
        if trecho_a_alterar is not None:
            # 2. Pede os NOVOS dados
            self.__tela_trecho.mostra_mensagem("\n--- Informe os Novos Dados para o Trecho ---")
            novos_dados = self.__tela_trecho.pega_dados_trecho()
            
            if novos_dados is None:
                self.__tela_trecho.mostra_mensagem("Alteração cancelada.")
                return

            trecho_a_alterar.data = novos_dados['data']
            trecho_a_alterar.origem = novos_dados['origem']
            trecho_a_alterar.destino = novos_dados['destino']
            trecho_a_alterar.transporte = novos_dados['transporte']
            trecho_a_alterar.valor_trecho = novos_dados['valor_trecho']
            
            self.__tela_trecho.mostra_mensagem('Trecho alterado com sucesso!')
            self.listar_trechos()
        else:
            self.__tela_trecho.mostra_mensagem('Erro: Trecho não encontrado para alteração.')


    def listar_trechos(self):
        self.__tela_trecho.mostra_mensagem("--- Lista de Trechos Registrados ---")
        if not self.__trechos:
            self.__tela_trecho.mostra_mensagem("Nenhum trecho registrado.")
            return
        for trecho in self.__trechos:
            self.__tela_trecho.mostra_trechos(trecho)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_trecho,
            2: self.excluir_trecho,
            3: self.alterar_trecho,
            4: self.listar_trechos
        }
        while True:
            opcao = self.__tela_trecho.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
