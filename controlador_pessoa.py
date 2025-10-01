from entidade.pessoa import Pessoa
from limite.tela_pessoa import TelaPessoa

class ControladorPessoas():
    def __init__(self, controlador_sistema):
        self.__tela_pessoa = TelaPessoa(self)
        self._pessoas = []
        self.__controlador_sistema = controlador_sistema
    
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
            nova_pessoa = Pessoa(dados_pessoa['nome'], dados_pessoa['celular'], dados_pessoa['identificacao'], dados_pessoa['idade'])
            self.__pessoas.append(nova_pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa cadastrada com sucesso!")
        else:
            self.__tela_pessoa.mostra_mensagem("Erro: Essa pessoa já está cadstrada!")
                return None
          
    def excluir_pessoa(self):
        self.lista_pessoas()
        identificacao = self.tela_pessoa.seleciona_pessoa()
        pessoa_a_remover = self.find_pessoa_by_identificacao(identificacao)
        if pessoa is not None:
            self.__pessoas.remove(pessoa_a_remover)
            self.tela_pessoa.mostra_mensagem('Pessoa removida com sucesso!')
        else:
            self.tela_pessoa.mostra_mensagem(f'Erro: essa pessoa NÃO está cadastrada!')
          
    def alterar_pessoa(self):
        self.__lista_pessoas()
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
            self.__tela_pessoa.mostra_pessoa({'nome': pessoa.nome, 'celular': pessoa.celular, 'identificacao': pessoa.identificacao, 'idade': idade})
    
    def valor_falta_pagar(self):
    
    def valor_pago(self):
    
    def verificar_se_pagou(self):
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {0: self.retornar, 1: self.inclui_pessoa, 2: self.exclui_pessoa,3: self.valor_falta_pagar, 4: self.valor_pago, 5: self.verificar_se_pagou}
        while True:
            opcao = self.__tela_pessoa.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes(opcao)
            funcao_escolhida()
    
