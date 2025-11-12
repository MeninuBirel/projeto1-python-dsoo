from entidade.trecho import Trecho
from limite.tela_trecho import TelaTrecho
from entidade.local import Local
from entidade.transporte import Transporte
from entidade.empresa import Empresa


class ControladorTrechos():
    def __init__(self, controlador_sistema):
        self.__tela_trecho = TelaTrecho(self)
        self.__trechos = []
        self.__controlador_sistema = controlador_sistema

    @property
    def trechos(self):
        return self.__trechos
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def find_trecho_no_sistema(self, data: str, origem: Local, destino: Local, transporte: Transporte, empresa: Empresa):
        for trecho in self.__trechos:
            if trecho.data == data and trecho.origem == origem and trecho.destino == destino and trecho.transporte == transporte and trecho.empresa == empresa:
                return trecho
        return None
    
    def find_trecho_na_viagem(self, viagem, data: str, origem: Local, destino: Local, transporte: Transporte, empresa: Empresa):
        for trecho in viagem.trechos:
            if trecho.data == data and trecho.origem == origem and trecho.destino == destino and trecho.transporte == transporte and trecho.empresa == empresa:
                return trecho
        return None
    
    def incluir_trecho(self):
        viagem = self.__tela_trecho.seleciona_qual_viagem()
        dados_trecho = self.__tela_trecho.pega_dados_trecho()
        origem_obj = dados_trecho['origem'] 
        destino_obj = dados_trecho['destino']
        trecho = self.find_trecho_na_viagem(viagem, dados_trecho['data'], origem_obj, destino_obj, dados_trecho['transporte'], dados_trecho['empresa'])
        if trecho is None:
            novo_trecho = Trecho(dados_trecho['data'], origem_obj, destino_obj,
                                 dados_trecho['transporte'], dados_trecho['empresa'], 
                                 dados_trecho['valor_trecho'])
            viagem.trechos.append(novo_trecho)
            self.__tela_trecho.mostra_mensagem('Trecho incluído com sucesso!')
            #adiciona no sistema geral
            if novo_trecho not in self.__trechos:
                self.__trechos.append(novo_trecho)
        else:
            self.__tela_trecho.mostra_mensagem('Erro: esse trecho já foi criado.')
        return None
    
    def excluir_trecho(self):
        viagem = self.__tela_trecho.seleciona_qual_viagem()
        self.listar_trechos(viagem)
        self.__tela_trecho.mostra_mensagem("\n--- Selecione o Trecho a ser Excluído ---")
        dados_selecao = self.__tela_trecho.pega_dados_trecho()
        if dados_selecao is None:
            self.__tela_trecho.mostra_mensagem("Exclusão cancelada.")
            return
        trecho_a_remover = self.find_trecho_na_viagem(
            viagem,
            dados_selecao['data'],
            dados_selecao['origem'],
            dados_selecao['destino'],
            dados_selecao['transporte'],
            dados_selecao['empresa']
        )
        if trecho_a_remover is not None:
            viagem.trechos.remove(trecho_a_remover)
            self.__tela_trecho.mostra_mensagem('Trecho removido com sucesso!')
        else:
            self.__tela_trecho.mostra_mensagem('Erro: O trecho com os dados informados NÃO está cadastrado!')
    
    def alterar_trecho(self):
        viagem = self.__tela_trecho.seleciona_qual_viagem()
        self.listar_trechos(viagem)

        self.__tela_trecho.mostra_mensagem("\n--- Identifique o Trecho a ser Alterado (Dados Atuais) ---")
        dados_identificacao = self.__tela_trecho.pega_dados_trecho()
        
        if dados_identificacao is None:
            self.__tela_trecho.mostra_mensagem("Alteração cancelada.")
            return

        trecho_a_alterar = self.find_trecho_no_sistema(
            dados_identificacao['data'],
            dados_identificacao['origem'],
            dados_identificacao['destino'],
            dados_identificacao['transporte'],
            dados_identificacao['empresa']
        )
        if trecho_a_alterar is not None:
            self.__tela_trecho.mostra_mensagem("\n--- Informe os Novos Dados para o Trecho ---")
            novos_dados = self.__tela_trecho.pega_dados_trecho()
            if novos_dados is None:
                self.__tela_trecho.mostra_mensagem("Alteração cancelada.")
                return
            #alterar na viagem
            for viagem in self.controlador_sistema.controlador_viagens.viagens:
                for tre in viagem.trechos:
                    if tre.data == trecho_a_alterar.data and tre.origem == trecho_a_alterar.origem and tre.destino == trecho_a_alterar.destino and tre.transporte == trecho_a_alterar.transporte and tre.empresa == trecho_a_alterar.empresa and tre.valor_trecho == trecho_a_alterar.valor_trecho:
                        tre.data = novos_dados['data']
                        tre.origem = novos_dados['origem']
                        tre.destino = novos_dados['destino']
                        tre.transporte = novos_dados['transporte']
                        tre.valor_trecho = novos_dados['valor_trecho']
            #alterar no sistema
            trecho_a_alterar.data = novos_dados['data']
            trecho_a_alterar.origem = novos_dados['origem']
            trecho_a_alterar.destino = novos_dados['destino']
            trecho_a_alterar.transporte = novos_dados['transporte']
            trecho_a_alterar.valor_trecho = novos_dados['valor_trecho']
            
            self.__tela_trecho.mostra_mensagem('Trecho alterado com sucesso!')
            self.listar_trechos(viagem)
        else:
            self.__tela_trecho.mostra_mensagem('Erro: Trecho não encontrado para alteração.')

    def listar_trechos(self, viagem):
        self.__tela_trecho.mostra_mensagem("--- Lista de Trechos Registrados ---")
        if not viagem.trechos:
            self.__tela_trecho.mostra_mensagem("Nenhum trecho registrado.")
            return
        for trecho in viagem.trechos:
            self.__tela_trecho.mostra_trechos(trecho)
    
    def listar_trechos_na_viagem(self):
        viagem = self.__tela_trecho.seleciona_qual_viagem()
        self.__tela_trecho.mostra_mensagem("--- Lista de Trechos Registrados ---")
        if not viagem.trechos:
            self.__tela_trecho.mostra_mensagem("Nenhum trecho registrado.")
            return
        for trecho in viagem.trechos:
            self.__tela_trecho.mostra_trechos(trecho)
    
    def listar_trechos_no_sistema(self):
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
            4: self.listar_trechos_na_viagem
        }
        while True:
            opcao = self.__tela_trecho.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
