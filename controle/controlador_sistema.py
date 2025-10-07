from controle.controlador_empresa import ControladorEmpresas
from controle.controlador_local import ControladorLocais
from controle.controlador_pagamento import ControladorPagamentos
from controle.controlador_passeio_turistico import ControladorPasseioTuristico
from controle.controlador_pessoa import ControladorPessoas
from controle.controlador_transporte import ControladorTransporte
from controle.controlador_trecho import ControladorTrechos
from controle.controlador_viagem import ControladorViagem
from limite.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_locais = ControladorLocais(self)
        self.__controlador_pessoas = ControladorPessoas(self)
        self.__controlador_transportes = ControladorTransporte(self)
        self.__controlador_empresas = ControladorEmpresas(self)
        self.__controlador_trechos = ControladorTrechos(self)
        self.__controlador_passeio_turistico = ControladorPasseioTuristico(self)
        self.__controlador_pagamentos = ControladorPagamentos(self)
        self.__controlador_viagem = ControladorViagem(self)

    @property
    def controlador_locais(self):
        return self.__controlador_locais

    @property
    def controlador_pessoas(self):
        return self.__controlador_pessoas

    @property
    def controlador_transportes(self):
        return self.__controlador_transportes

    @property
    def controlador_empresas(self):
        return self.__controlador_empresas

    @property
    def controlador_trechos(self):
        return self.__controlador_trechos

    @property
    def controlador_passeios_turisticos(self):
        return self.__controlador_passeio_turistico  # Corrigido para o nome da variável de instância

    @property
    def controlador_pagamentos(self):
        return self.__controlador_pagamentos

    @property
    def controlador_viagem(self):
        return self.__controlador_viagem

    def inicializa_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        self.__tela_sistema.mostra_mensagem('Sistema Encerrado! Volte Sempre!')
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_pessoas,
            2: self.cadastra_locais,
            3: self.cadastra_transportes,
            4: self.cadastra_empresas,
            5: self.cadastra_trechos,
            6: self.cadastra_passeios_turisticos,
            7: self.cadastra_pagamentos,
            8: self.ver_infos_viagem,
            0: self.encerra_sistema
        }
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_pessoas(self):  # chama o controlador de pessoas
        self.__controlador_pessoas.abre_tela()

    def cadastra_locais(self):
        self.__controlador_locais.abre_tela()

    def cadastra_transportes(self):
        self.__controlador_transportes.abre_tela()

    def cadastra_empresas(self):
        self.__controlador_empresas.abre_tela()

    def cadastra_trechos(self):
        self.__controlador_trechos.abre_tela()

    def cadastra_passeios_turisticos(self):
        self.__controlador_passeios_turisticos.abre_tela()

    def cadastra_pagamentos(self):
        self.__controlador_pagamentos.abre_tela()

    def ver_infos_viagem(self):
        self.__controlador_viagem.abre_tela() # O código original termina aqui
