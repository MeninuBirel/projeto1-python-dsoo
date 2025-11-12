from limite.tela_pagamento import TelaPagamento
from entidade.pix import Pix
from entidade.dinheiro import Dinheiro
from entidade.cartao import Cartao
from entidade.pagamento import Pagamento


class ControladorPagamentos():
    def __init__(self, controlador_sistema):
        self.__tela_pagamento = TelaPagamento(self)
        self.__pagamentos = []  # lista geral de Pagamento (inclui Pix, Dinheiro, Cartao)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_pessoas = controlador_sistema.controlador_pessoas

    @property
    def pagamentos(self):
        return self.__pagamentos
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def incluir_pagamento(self):
        viagem = self.__tela_pagamento.seleciona_qual_viagem()
        pessoas_cadastradas = viagem.pessoas
        pessoa_selecionada = self.__tela_pagamento.seleciona_pessoa_pagamento(pessoas_cadastradas)

        if pessoa_selecionada is None:
            self.__tela_pagamento.mostra_mensagem("Operação cancelada ou nenhuma pessoa selecionada.")
            return
        dados_pagamento = self.__tela_pagamento.pega_dados_pagamento(pessoa_selecionada)

        try:
            novo_pagamento: Pagamento = None

            if dados_pagamento['tipo'] == 'PIX':
                novo_pagamento = Pix(
                    dados_pagamento['valor'],
                    dados_pagamento['pessoa'],
                    dados_pagamento['data'],
                    dados_pagamento['cpf']
                )
            elif dados_pagamento['tipo'] == 'DINHEIRO':
                novo_pagamento = Dinheiro(
                    dados_pagamento['valor'],
                    dados_pagamento['pessoa'],
                    dados_pagamento['data'],
                    dados_pagamento['cpf']
                )
            elif dados_pagamento['tipo'] == 'CARTAO':
                novo_pagamento = Cartao(
                    dados_pagamento['valor'],
                    dados_pagamento['pessoa'],
                    dados_pagamento['data'],
                    dados_pagamento['numero_cartao'],
                    dados_pagamento['bandeira']
                )

            if novo_pagamento:
                viagem.pagamentos.append(novo_pagamento)
                if novo_pagamento not in self.__pagamentos:
                    self.__pagamentos.append(novo_pagamento)
                self.__tela_pagamento.mostra_mensagem(
                    f"Pagamento via {dados_pagamento['tipo']} de R$ {dados_pagamento['valor']:.2f} registrado com sucesso!")

        except (ValueError, TypeError) as e:
            self.__tela_pagamento.mostra_mensagem(f"Erro ao registrar pagamento: {e}")
        except Exception as e:
            self.__tela_pagamento.mostra_mensagem(f"Erro inesperado: {e}")
    
    def listar_pagamentos(self):
        viagem = self.__tela_pagamento.seleciona_qual_viagem()
        self.__tela_pagamento.mostra_mensagem("--- Lista de Pagamentos Registrados ---")
        if not viagem.pagamentos:
            self.__tela_pagamento.mostra_mensagem("Nenhum pagamento registrado.")
            return
        for pagamento in viagem.pagamentos:
            self.__tela_pagamento.mostra_pagamento(pagamento)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_pagamento,
            2: self.listar_pagamentos
        }

        while True:
            opcao = self.__tela_pagamento.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
        
