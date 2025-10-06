from entidade.passeio_turistico import PasseioTuristico
from limite.tela_passeio_turistico import TelaPasseioTuristico


class ControladorPasseioTuristico():
    def __init__(self, controlador_sistema):
        self.__tela_passeio_turistico = TelaPasseioTuristico(self)
        self.__passeios_turisticos = []
        self.__controlador_sistema = controlador_sistema

    @property
    def passeios(self):
        return self.__passeios_turisticos

    def find_passeio_by_atracao(self, atracao_turistica: str):
        for passeio in self.__passeios_turisticos:
            if passeio.atracao_turistica == atracao_turistica:
                return passeio

    def incluir_passeio(self):
        dados_passeio = self.__tela_passeio_turistico.pega_dados_passeio()
        atracao = dados_passeio['atracao_turistica']
        passeio = self.find_passeio_by_atracao(atracao)
        if passeio is None:
            novo_passeio = PasseioTuristico(
                dados_passeio['dia'],
                dados_passeio['cidade'],
                dados_passeio['atracao_turistica'],
                dados_passeio['horario_inc'],
                dados_passeio['horario_fim'],
                dados_passeio['valor_passeio']
            )
            self.__passeios_turisticos.append(novo_passeio)
            self.__tela_passeio_turistico.mostra_mensagem("Passeio cadastrado com sucesso!")
        else:
            self.__tela_passeio_turistico.mostra_mensagem("Erro: Esse passeio já está cadastrado!")
        return None

    def excluir_passeio(self):
        self.lista_passeios()
        atracao = self.tela_passeio_turistico.seleciona_passeio()
        passeio_a_remover = self.find_passeio_by_atracao(atracao)
        if passeio_a_remover is not None:
            self.__passeios_turisticos.remove(passeio_a_remover)
            self.__tela_passeio_turistico.mostra_mensagem('Passeio removido com sucesso!')
        else:
            self.__tela_passeio_turistico.mostra_mensagem(f'Erro: esse passeio NÃO está cadastrado!')

    def lista_passeios(self):
        for passeio in self.__passeios_turisticos:
            self.__tela_passeio_turistico.mostra_passeio({
                'dia': passeio.dia,
                'cidade': passeio.cidade,
                'atracao_turistica': passeio.atracao_turistica,
                'horario_inc': passeio.horario_inc,
                'horario_fim': passeio.horario_fim,
                'valor_passeio': passeio.valor_passeio
            })

    def listar_passeios(self):
        self.__tela_passeio_turistico.mostra_mensagem("--- Lista de Passeios Turísticos Registrados ---")
        if not self.__passeios_turisticos:
            self.__tela_passeio_turistico.mostra_mensagem("Nenhum passeio turístico registrado.")
            return
        for passeio in self.__passeios_turisticos:
            self.__tela_passeio_turistico.mostra_passeios(passeio)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_passeio,
            2: self.excluir_passeio,
            3: self.listar_passeios
        }
        while True:
            opcao = self.__tela_passeio_turistico.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
