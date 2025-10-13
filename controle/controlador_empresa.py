from limite.tela_empresa import TelaEmpresa
from entidade.empresa import Empresa


class ControladorEmpresas():
    def __init__(self, controlador_sistema):
        self.__tela_empresa = TelaEmpresa(self)
        self.__empresas = []
        self.__controlador_sistema = controlador_sistema
    
    @property
    def empresas(self):
        return self.__empresas
    
    def find_empresa_by_cnpj(self, cnpj: str):
        for empresa in self.__empresas:
            if empresa.cnpj == cnpj:
                return empresa
        return None
    
    def incluir_empresa(self):
        dados_empresa = self.__tela_empresa.pega_dados_empresa()
        cnpj = dados_empresa['cnpj']
        empresa = self.find_empresa_by_cnpj(cnpj)
        if empresa is None:
            nova_empresa = Empresa(dados_empresa['nome'], dados_empresa['cnpj'],
                                 dados_empresa['telefone'])
            self.__empresas.append(nova_empresa)
            self.__tela_empresa.mostra_mensagem("Empresa cadastrada com sucesso!")
        else:
            self.__tela_empresa.mostra_mensagem("Erro: Essa empresa já está cadastrada!")
        return None

    def excluir_empresa(self):
        self.lista_empresas()
        cnpj = self.__tela_empresa.seleciona_empresa()
        empresa_a_remover = self.find_empresa_by_cnpj(cnpj)
        if empresa_a_remover is not None:
            self.__empresas.remove(empresa_a_remover)
            self.__tela_empresa.mostra_mensagem('Empresa removida com sucesso!')
        else:
            self.__tela_empresa.mostra_mensagem(f'Erro: essa empresa NÃO está cadastrada!')
    
    def alterar_empresa(self):
        self.lista_empresas()
        cnpj_empresa = self.__tela_empresa.seleciona_empresa()
        empresa = self.find_empresa_by_cnpj(cnpj_empresa)
        if empresa is not None:
            novos_dados = self.__tela_empresa.pega_dados_empresa()
            empresa.nome = novos_dados['nome']
            empresa.cnpj = novos_dados['cnpj']
            empresa.telefone = novos_dados['telefone']
            self.lista_empresas()
        else:
            self.__tela_empresa.mostra_mensagem('Erro: empresa não está cadastrada')
    
    def lista_empresas(self):
        for empresa in self.__empresas:
            self.__tela_empresa.mostra_empresa({
                'nome': empresa.nome,
                'cnpj': empresa.cnpj,
                'telefone': empresa.telefone
            })

    def listar_empresas(self):
        self.__tela_empresa.mostra_mensagem("--- Lista de Empresas Registradas ---")
        if not self.__empresas:
            self.__tela_empresa.mostra_mensagem("Nenhuma empresa registrada.")
            return
        for empresa in self.__empresas:
            self.__tela_empresa.mostra_empresas(empresa)
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()
        
    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_empresa,
            2: self.excluir_empresa,
            3: self.alterar_empresa,
            4: self.listar_empresas
        }
        while True:
            opcao = self.__tela_empresa.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
