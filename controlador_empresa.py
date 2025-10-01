from limite.tela_empresa import TelaEmpresa
from entidade.empresa import Empresa


class ControladorEmpresas:
    def __init__(self, controlador_sistema):
        self.__tela_empresa = TelaEmpresa()
        self.__empresas = []
        self.__controlador_sistema = controlador_sistema

    def cadastrar_empresa(self): #verificar se não há empresas repetidas!!!!
        dados = self.tela.pega_dados_empresa()
        try:
            nova_empresa = Empresa(dados["nome"], dados["cnpj"], dados["telefone"])
            self.empresas.append(nova_empresa)
            self.tela.mostra_mensagem("Empresa cadastrada com sucesso!")
        except (ValueError, TypeError) as e:
            self.tela.mostra_mensagem(f"Erro ao cadastrar: {e}")

    def listar_empresas(self):
        self.tela.mostra_empresas(self.empresas)

    def ver_detalhes_empresa(self):
        if not self.empresas:
            self.tela.mostra_mensagem("Nenhuma empresa cadastrada.")
            return

        empresa_selecionada = self.tela.seleciona_empresa(self.empresas)
        if empresa_selecionada:
            self.tela.mostra_detalhes_empresa(empresa_selecionada)

    def iniciar(self):
        while True:
            opcao = self.tela.menu_empresa()

            if opcao == 1:
                self.cadastrar_empresa()
            elif opcao == 2:
                self.listar_empresas()
            elif opcao == 3:
                self.ver_detalhes_empresa()
            elif opcao == 0:
                break
            else:
                self.tela.mostra_mensagem("Opção inválida!")
