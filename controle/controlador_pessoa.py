from entidade.pessoa import Pessoa
from limite.tela_pessoa import TelaPessoa


class ControladorPessoas():
    def __init__(self, controlador_sistema):
        self.__tela_pessoa = TelaPessoa(self)
        self.__pessoas = []
        self.__controlador_sistema = controlador_sistema

    @property
    def pessoas(self):
        return self.__pessoas

    def find_pessoa_by_identificacao(self, identificacao: str):
        for pessoa in self.__pessoas:
            if pessoa.identificacao == identificacao:
                return pessoa
        return None

    def incluir_pessoa(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        identificacao = dados_pessoa['identificacao']
        pessoa = self.find_pessoa_by_identificacao(identificacao)
        if pessoa is None:
            nova_pessoa = Pessoa(dados_pessoa['nome'], dados_pessoa['celular'],
                                 dados_pessoa['identificacao'], dados_pessoa['idade'])
            self.__pessoas.append(nova_pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa cadastrada com sucesso!")
        else:
            self.__tela_pessoa.mostra_mensagem("Erro: Essa pessoa já está cadastrada!")
        return None

    def excluir_pessoa(self):
        self.lista_pessoas()
        identificacao = self.__tela_pessoa.seleciona_pessoa()
        pessoa_a_remover = self.find_pessoa_by_identificacao(identificacao)
        if pessoa_a_remover is not None:
            self.__pessoas.remove(pessoa_a_remover)
            self.__tela_pessoa.mostra_mensagem('Pessoa removida com sucesso!')
        else:
            self.__tela_pessoa.mostra_mensagem(f'Erro: essa pessoa NÃO está cadastrada!')

    def alterar_pessoa(self):
        self.lista_pessoas()
        identificacao_pessoa = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.find_pessoa_by_identificacao(identificacao_pessoa)
        if pessoa is not None:
            novos_dados = self.__tela_pessoa.pega_dados_pessoa()
            pessoa.nome = novos_dados['nome']
            pessoa.celular = novos_dados['celular']
            pessoa.identificacao = novos_dados['identificacao']
            pessoa.idade = novos_dados['idade']
            self.lista_pessoas()
        else:
            self.__tela_pessoa.mostra_mensagem('Erro: pessoa não está cadastrada')

    def lista_pessoas(self):
        for pessoa in self.__pessoas:
            self.__tela_pessoa.mostra_pessoa({
                'nome': pessoa.nome,
                'celular': pessoa.celular,
                'identificacao': pessoa.identificacao,
                'idade': pessoa.idade
            })
            
    def listar_pessoas(self):
        self.__tela_pessoa.mostra_mensagem("--- Lista de Pessoas Registradas ---")
        if not self.__pessoas:
            self.__tela_pessoa.mostra_mensagem("Nenhuma pessoa registrada.")
            return
        for pessoa in self.__pessoas:
            self.__tela_pessoa.mostra_pessoas(pessoa)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_pessoa,
            2: self.excluir_pessoa,
            3: self.alterar_pessoa,
            4: self.listar_pessoas
        }
        while True:
            opcao = self.__tela_pessoa.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()

    
