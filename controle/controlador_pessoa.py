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
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def find_pessoa_by_identificacao(self, identificacao: int):
        for pessoa in self.__pessoas:
            if pessoa.identificacao == identificacao:
                return pessoa
        return None
    
    def find_pessoa_by_identificacao_na_viagem(self, viagem, identificacao: int):
        for pessoa in viagem.pessoas:
            if pessoa.identificacao == identificacao:
                return pessoa
        return None
    
    def incluir_pessoa(self):
        viagem = self.__tela_pessoa.seleciona_qual_viagem() #adicionar pessoa numa viagem especifica
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        identificacao = dados_pessoa['identificacao']
        nome = dados_pessoa['nome']
        celular = dados_pessoa['celular']
        idade = dados_pessoa['idade']

        pessoa_no_sistema = self.find_pessoa_by_identificacao(identificacao)
        if pessoa_no_sistema:
            if pessoa_no_sistema.nome == nome and pessoa_no_sistema.celular == celular and pessoa_no_sistema.idade == idade:
                pessoa = self.find_pessoa_by_identificacao_na_viagem(viagem, identificacao)
                if pessoa is None:
                    nova_pessoa = Pessoa(dados_pessoa['nome'], dados_pessoa['celular'],
                                 dados_pessoa['identificacao'], dados_pessoa['idade'])
                    viagem.pessoas.append(nova_pessoa) #adicionar pessoa na viagem especifica
                    self.__tela_pessoa.mostra_mensagem("Pessoa cadastrada com sucesso!")
                else:
                    self.__tela_pessoa.mostra_mensagem("Erro: Essa pessoa já está cadastrada!")
            else:
                self.__tela_pessoa.mostra_mensagem("Erro: Essa dentificação já está sendo usada para outro usuário!")
        else:
            pessoa = self.find_pessoa_by_identificacao_na_viagem(viagem, identificacao)
            if pessoa is None:
                nova_pessoa = Pessoa(dados_pessoa['nome'], dados_pessoa['celular'],
                                 dados_pessoa['identificacao'], dados_pessoa['idade'])
                viagem.pessoas.append(nova_pessoa) #adicionar pessoa na viagem especifica
                self.__tela_pessoa.mostra_mensagem("Pessoa cadastrada com sucesso!")
                #adicionar no sistema geral
                self.__pessoas.append(nova_pessoa)
        return None
        
    
    def excluir_pessoa_da_viagem(self):
        viagem = self.__tela_pessoa.seleciona_qual_viagem()
        self.listar_pessoas(viagem)
        identificacao = self.__tela_pessoa.seleciona_pessoa()
        pessoa_a_remover = self.find_pessoa_by_identificacao_na_viagem(viagem, identificacao)
        if pessoa_a_remover is not None:
            viagem.pessoas.remove(pessoa_a_remover)
            self.__tela_pessoa.mostra_mensagem('Pessoa removida com sucesso!')
        else:
            self.__tela_pessoa.mostra_mensagem(f'Erro: essa pessoa NÃO está cadastrada!')
    
    def excluir_pessoa_do_sistema(self):
        self.listar_pessoas_no_sistema()
        identificacao = self.__tela_pessoa.seleciona_pessoa()
        pessoa_a_remover = self.find_pessoa_by_identificacao(identificacao)
        if pessoa_a_remover is not None:
            self.__pessoas.remove(pessoa_a_remover)
            self.__tela_pessoa.mostra_mensagem('Pessoa removida com sucesso!')
        else:
            self.__tela_pessoa.mostra_mensagem(f'Erro: essa pessoa NÃO está cadastrada!')
    
    def alterar_pessoa(self):
        self.listar_pessoas_no_sistema()
        identificacao_pessoa = self.__tela_pessoa.seleciona_pessoa()
        #alterar no sistema
        pessoa = self.find_pessoa_by_identificacao(identificacao_pessoa)
        if pessoa is not None:
            novos_dados = self.__tela_pessoa.pega_dados_pessoa()
            #alterar nas viagens
            for viagem in self.controlador_sistema.controlador_viagens.viagens:
                for pes in viagem.pessoas:
                    if pes.nome == pessoa.nome and pes.celular == pessoa.celular and pes.identificacao == pessoa.identificacao and pes.idade == pessoa.idade:
                        pes.nome = novos_dados['nome']
                        pes.celular = novos_dados['celular']
                        pes.identificacao = novos_dados['identificacao']
                        pes.idade = novos_dados['idade']
            #alterar no sistema
            pessoa.nome = novos_dados['nome']
            pessoa.celular = novos_dados['celular']
            pessoa.identificacao = novos_dados['identificacao']
            pessoa.idade = novos_dados['idade']
            self.listar_pessoas_no_sistema()
        else:
            self.__tela_pessoa.mostra_mensagem('Erro: pessoa não está cadastrada')
    
    def listar_pessoas_no_sistema(self):
        self.__tela_pessoa.mostra_mensagem("--- Lista de Pessoas Registradas no Sistema ---")
        if not self.__pessoas:
            self.__tela_pessoa.mostra_mensagem("Nenhuma pessoa registrada.")
            return
        for pessoa in self.__pessoas:
            self.__tela_pessoa.mostra_pessoas(pessoa)
    
    def listar_pessoas_na_viagem(self):
        viagem = self.__tela_pessoa.seleciona_qual_viagem()
        self.__tela_pessoa.mostra_mensagem("--- Lista de Pessoas Registradas na Viagem ---")
        if not viagem.pessoas:
            self.__tela_pessoa.mostra_mensagem("Nenhuma pessoa registrada.")
            return
        for pessoa in viagem.pessoas:
            self.__tela_pessoa.mostra_pessoas(pessoa)
    
    def listar_pessoas(self, viagem):
        self.__tela_pessoa.mostra_mensagem("--- Lista de Pessoas Registradas na Viagem ---")
        if not viagem.pessoas:
            self.__tela_pessoa.mostra_mensagem("Nenhuma pessoa registrada.")
            return
        for pessoa in viagem.pessoas:
            self.__tela_pessoa.mostra_pessoas(pessoa)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_pessoa,
            2: self.excluir_pessoa_da_viagem,
            3: self.excluir_pessoa_do_sistema,
            4: self.alterar_pessoa,
            5: self.listar_pessoas_na_viagem,
            6: self.listar_pessoas_no_sistema
        }
        while True:
            opcao = self.__tela_pessoa.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
