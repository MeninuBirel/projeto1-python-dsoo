from entidade.passeio_turistico import PasseioTuristico
from limite.tela_passeio_turistico import TelaPasseioTuristico


class ControladorPasseioTuristicos():
    def __init__(self, controlador_sistema):
        self.__tela_passeio_turistico = TelaPasseioTuristico(self)
        self.__passeios_turisticos = []
        self.__controlador_sistema = controlador_sistema

    @property
    def passeios(self):
        return self.__passeios_turisticos
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def find_passeio_by_atracao(self, atracao_turistica: str):
        for passeio in self.__passeios_turisticos:
            if passeio.atracao_turistica == atracao_turistica:
                return passeio
        return None
    
    def find_passeio_by_atracao_na_viagem(self, viagem, atracao_turistica: str):
        for passeio in viagem.passeios_turisticos:
            if passeio.atracao_turistica == atracao_turistica:
                return passeio
        return None
    
    def incluir_passeio(self):
        viagem = self.__tela_passeio_turistico.seleciona_qual_viagem()
        dados_passeio = self.__tela_passeio_turistico.pega_dados_passeio()
        atracao = dados_passeio['atracao_turistica']
        passeio = self.find_passeio_by_atracao_na_viagem(viagem, atracao)
        if passeio is None:
            novo_passeio = PasseioTuristico(
                dados_passeio['dia'],
                dados_passeio['cidade'],
                dados_passeio['atracao_turistica'],
                dados_passeio['horario_inc'],
                dados_passeio['horario_fim'],
                dados_passeio['valor_passeio']
            )
            viagem.passeios_turisticos.append(novo_passeio)
            self.__tela_passeio_turistico.mostra_mensagem("Passeio cadastrado com sucesso!")
            #adicionar no sistema geral
            if novo_passeio not in self.__passeios_turisticos:
                self.__passeios_turisticos.append(novo_passeio)
        else:
            self.__tela_passeio_turistico.mostra_mensagem("Erro: Esse passeio já está cadastrado!")
        return None
    
    def excluir_passeio(self):
        viagem = self.__tela_passeio_turistico.seleciona_qual_viagem()
        self.listar_passeios(viagem)
        atracao = self.__tela_passeio_turistico.seleciona_passeio()
        passeio_a_remover = self.find_passeio_by_atracao_na_viagem(viagem, atracao)
        if passeio_a_remover is not None:
            viagem.passeios_turisticos.remove(passeio_a_remover)
            self.__tela_passeio_turistico.mostra_mensagem('Passeio removido com sucesso!')
        else:
            self.__tela_passeio_turistico.mostra_mensagem(f'Erro: esse passeio NÃO está cadastrado!')
    
    def alterar_passeio(self):
        viagem = self.__tela_passeio_turistico.seleciona_qual_viagem()
        self.listar_passeios(viagem)
        identificacao_passeio = self.__tela_passeio_turistico.seleciona_passeio()
        passeio = self.find_passeio_by_atracao(identificacao_passeio)
        if passeio is not None:
            novos_dados = self.__tela_passeio_turistico.pega_dados_passeio()
            #alterar nas viagens
            for viagem in self.controlador_sistema.controlador_viagem.viagens:
                for pas in viagem.passeios:
                    if pas.dia == passeio.dia and pas.cidade == passeio.dia and pas.atracao_turistica == passeio.atracao_turistica and pas.horario_inc == passeio.horario_inc and pas.horario_fim == passeio.horario_fim and pas.valor_passeio == passeio.valor_passeio:
                        pas.dia = novos_dados['dia']
                        pas.cidade = novos_dados['cidade']
                        pas.atracao_turistica = novos_dados['atracao_turistica']
                        pas.horario_inc = novos_dados['horario_inc']
                        pas.horario_fim = novos_dados['horario_fim']
                        pas.valor_passeio = novos_dados['valor_passeio']
            #alterar no sistema
            passeio.dia = novos_dados['dia']
            passeio.cidade = novos_dados['cidade']
            passeio.atracao_turistica = novos_dados['atracao_turistica']
            passeio.horario_inc = novos_dados['horario_inc']
            passeio.horario_fim = novos_dados['horario_fim']
            passeio.valor_passeio = novos_dados['valor_passeio']
            self.listar_passeios(viagem)
        else:
            self.__tela_passeio_turistico.mostra_mensagem('Erro: passeio não está cadastrad0')
    
    def listar_passeios_do_sistema(self):
        self.__tela_passeio_turistico.mostra_mensagem("--- Lista de Passeios Turísticos Registrados ---")
        if not self.__passeios_turisticos:
            self.__tela_passeio_turistico.mostra_mensagem("Nenhum passeio turístico registrado.")
            return
        for passeio in self.__passeios_turisticos:
            self.__tela_passeio_turistico.mostra_passeios(passeio)
    
    def listar_passeios_da_viagem(self):
        viagem = self.__tela_passeio_turistico.seleciona_qual_viagem()
        self.__tela_passeio_turistico.mostra_mensagem("--- Lista de Passeios Turísticos Registrados na Viagem---")
        if not viagem.passeios_turisticos:
            self.__tela_passeio_turistico.mostra_mensagem("Nenhum passeio turístico registrado.")
            return
        for passeio in viagem.passeios_turisticos:
            self.__tela_passeio_turistico.mostra_passeios(passeio)
    
    def listar_passeios(self, viagem):
        self.__tela_passeio_turistico.mostra_mensagem("--- Lista de Passeios Turísticos Registrados na Viagem---")
        if not viagem.passeios_turisticos:
            self.__tela_passeio_turistico.mostra_mensagem("Nenhum passeio turístico registrado.")
            return
        for passeio in viagem.passeios_turisticos:
            self.__tela_passeio_turistico.mostra_passeios(passeio)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_passeio,
            2: self.excluir_passeio,
            3: self.alterar_passeio,
            4: self.listar_passeios_da_viagem
        }
        while True:
            opcao = self.__tela_passeio_turistico.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
    
