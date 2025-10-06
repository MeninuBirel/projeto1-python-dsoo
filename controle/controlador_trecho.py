from entidade.trecho import Trecho
from limite.tela_trecho import TelaTrecho
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

    def incluir_trecho(self):
        dados_trecho = self.__tela_trecho.pega_dados_trecho()
        novo_trecho = Trecho(
            dados_trecho['data'],
            dados_trecho['cidade_origem'],
            dados_trecho['pais_origem'],
            dados_trecho['cidade_destino'],
            dados_trecho['pais_destino'],
            dados_trecho['transporte'],
            dados_trecho['valor_trecho']
        )
        for trecho_existente in self.trechos:
            if (trecho_existente.data == dados_trecho['data'] and
                trecho_existente.cidade_origem == dados_trecho['cidade_origem'] and
                trecho_existente.cidade_destino == dados_trecho['cidade_destino'] and
                    trecho_existente.transporte == dados_trecho['transporte']):
                self.__tela_trecho.mostra_mensagem('Erro: esse trecho já foi criado.')
                return None
        self.__trechos.append(novo_trecho)
        self.__tela_trecho.mostra_mensagem('Trecho incluído com sucesso!')

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
            2: self.listar_trechos
        }
        while True:
            opcao = self.__tela_trecho.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
