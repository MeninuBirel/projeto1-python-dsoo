from limite.tela_transporte import TelaTransporte
from entidade.transporte import Transporte

class ControladorTransporte:
    def __init__(self, controlador_empresa):
        self.tela = TelaTransporte()
        self.controlador_empresa = controlador_empresa
        self.transportes = []

    def cadastrar_transporte(self):
        empresas_disponiveis = self.controlador_empresa.empresas
        if not empresas_disponiveis:
            self.tela.mostra_mensagem("Erro: Nenhuma empresa cadastrada. Cadastre uma empresa primeiro.")
            return

        dados = self.tela.pega_dados_transporte(empresas_disponiveis)

        try:
            empresa_selecionada = dados["empresa"]
            novo_transporte = Transporte(
                dados["tipo"],
                empresa_selecionada,
                dados["valor"]
            )
            self.transportes.append(novo_transporte)
            empresa_selecionada.adicionar_transporte(novo_transporte)
            self.tela.mostra_mensagem("Transporte cadastrado com sucesso!")
        except (ValueError, TypeError) as e:
            self.tela.mostra_mensagem(f"Erro ao cadastrar: {e}")

    def listar_transportes(self):
        self.tela.mostra_transportes(self.transportes)

    def abre_tela(self):
        while True:
            opcao = self.tela.menu_transporte()

            if opcao == 1:
                self.cadastrar_transporte()
            elif opcao == 2:
                self.listar_transportes()
            elif opcao == 0:
                break
            else:
                self.tela.mostra_mensagem("Opção inválida!")
