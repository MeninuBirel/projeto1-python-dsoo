from limite.tela_empresa import TelaEmpresa
from entidade.empresa import Empresa


class ControladorEmpresas:
    def __init__(self, controlador_sistema):
        self.__tela_empresa = TelaEmpresa(self)
        self.__empresas = []
        self.__controlador_sistema = controlador_sistema

    def cadastrar_empresa(self): #verificar se não há empresas repetidas!!!!
        dados = self.tela_empresa.pega_dados_empresa()
        try:
            nova_empresa = Empresa(dados["nome"], dados["cnpj"], dados["telefone"])
            self.__empresas.append(nova_empresa)
            self.tela_empresa.mostra_mensagem("Empresa cadastrada com sucesso!")
        except (ValueError, TypeError) as e:
            self.tela_empresa.mostra_mensagem(f"Erro ao cadastrar: {e}")

    def listar_empresas(self):
        self.tela_empresa.mostra_empresas(self.__empresas)

    def ver_detalhes_empresa(self):
        if not self.__empresas:
            self.tela_empresa.mostra_mensagem("Nenhuma empresa cadastrada.")
            return

        empresa_selecionada = self.tela_empresa.seleciona_empresa(self.__empresas)
        if empresa_selecionada:
            self.tela_empresa.mostra_detalhes_empresa(empresa_selecionada)
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()
        
    def abre_tela(self):
        while True:
            opcao = self.tela_empresa.menu_empresa()

            if opcao == 1:
                self.cadastrar_empresa()
            elif opcao == 2:
                self.listar_empresas()
            elif opcao == 3:
                self.ver_detalhes_empresa()
            elif opcao == 0:
                self.retornar()
            else:
                self.tela_empresa.mostra_mensagem("Opção inválida!")
