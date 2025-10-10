from entidade.viagem import Viagem
from limite.tela_viagem import TelaViagem
from collections import defaultdict


class ControladorViagem:
    def __init__(self, controlador_sistema):
        self.__tela_viagem = TelaViagem(self)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_trechos = controlador_sistema.controlador_trechos
        self.__controlador_passeio_turistico = controlador_sistema.controlador_passeio_turistico
        self.__controlador_pessoas = controlador_sistema.controlador_pessoas
        self.__controlador_pagamentos = controlador_sistema.controlador_pagamentos

    def valor_total_por_pessoa(self):
        total_por_pessoa = 0.0
        for trecho in self.__controlador_trechos.trechos:
            total_por_pessoa += trecho.valor_trecho

        for passeio in self.__controlador_passeio_turistico.passeios:
            total_por_pessoa += passeio.valor_passeio

        return total_por_pessoa

    def exibir_valor_total_por_pessoa(self):
        """Chama o cálculo e exibe o resultado para o usuário."""
        total = self.valor_total_por_pessoa()
        self.__tela_viagem.mostra_mensagem(f'O valor do pacote para cada pessoa é R$ {total:.2f}')
        return total

    def valor_total(self):
        total_pessoa = self.valor_total_por_pessoa()
        numero_pessoas = len(self.__controlador_pessoas.pessoas)
        total = total_pessoa * numero_pessoas
        return total

    def exibir_valor_total(self):
        """Chama o cálculo e exibe o resultado para o usuário."""
        total = self.valor_total()
        numero_pessoas = len(self.__controlador_pessoas.pessoas)
        self.__tela_viagem.mostra_mensagem(
            f'Com um total de {numero_pessoas} participantes, o valor total da viagem é R$ {total:.2f}')
        return total

    def valor_pago(self):
        total_pago = sum(pagamento.valor for pagamento in self.__controlador_pagamentos.pagamentos)
        total_viagem = self.valor_total()

        self.__tela_viagem.mostra_mensagem("\n--- Status de Pagamento Geral ---")
        self.__tela_viagem.mostra_mensagem(f'Total já pago por todos: R$ {total_pago:.2f}')
        self.__tela_viagem.mostra_mensagem(f'Valor total necessário: R$ {total_viagem:.2f}')

        if total_pago < total_viagem:
            self.__tela_viagem.mostra_mensagem(f'Falta pagar: R$ {total_viagem - total_pago:.2f}')
        elif total_pago > total_viagem:
            self.__tela_viagem.mostra_mensagem(f'Valor excedente pago: R$ {total_pago - total_viagem:.2f}')
        else:
            self.__tela_viagem.mostra_mensagem('O valor total da viagem foi integralmente pago!')

        return total_pago

    def verificar_quem_pagou(self):
        # Obtém o valor total que cada pessoa deve pagar
        valor_por_pessoa = self.valor_total_por_pessoa()
        
        # Agrega o total de pagamentos por pessoa
        # Cria um dicionário para somar o total pago por cada pessoa.
        pagamentos_pessoa = defaultdict(float)
        for pagamento in self.__controlador_pagamentos.pagamentos:
            # Para cada pagamento, acessa a identificação da pessoa pagadora e soma
            # o valor pago ao total acumulado para aquela pessoa no dicionário.
            identificacao = pagamento.pessoa.identificacao
            pagamentos_pessoa[identificacao] += pagamento.valor

        pessoas_pagaram = []
        pessoas_cadastradas = self.__controlador_pessoas.pessoas

        self.__tela_viagem.mostra_mensagem("\n--- Pessoas que Pagaram o Pacote Completo ---")
        if not pessoas_cadastradas:
            self.__tela_viagem.mostra_mensagem("Nenhuma pessoa cadastrada para verificar pagamentos.")
            return []

        # Inicia o processo de verificação individual para cada pessoa cadastrada.
        for pessoa in pessoas_cadastradas:
            # Obtém o valor total pago por essa pessoa.
            total_pago = pagamentos_pessoa[pessoa.identificacao]

            # Checa se o valor pago é maior ou igual ao valor por pessoa
            if total_pago >= valor_por_pessoa:
                pessoas_pagaram.append(pessoa)
                self.__tela_viagem.mostra_mensagem(f"- {pessoa.nome} (Pago: R$ {total_pago:.2f})")

        # Se a lista de pagadores integrais ficou vazia, exibe uma mensagem.
        if not pessoas_pagaram:
            self.__tela_viagem.mostra_mensagem("Nenhuma pessoa pagou o valor completo do pacote ainda.")

    def verificar_quem_nao_pagou(self):
        valor_por_pessoa = self.valor_total_por_pessoa()

        pagamentos_pessoa = defaultdict(float)
        for pagamento in self.__controlador_pagamentos.pagamentos:
            identificacao = pagamento.pessoa.identificacao
            pagamentos_pessoa[identificacao] += pagamento.valor

        pessoas_nao_pagaram = []
        pessoas_cadastradas = self.__controlador_pessoas.pessoas
        self.__tela_viagem.mostra_mensagem("\n--- Pessoas com Pagamento Pendente ---")

        if not pessoas_cadastradas:
            self.__tela_viagem.mostra_mensagem("Nenhuma pessoa cadastrada para verificar pagamentos.")
            return []
            
        for pessoa in pessoas_cadastradas:
            total_pago = pagamentos_pessoa[pessoa.identificacao]

            # Checa se o valor pago é menor que o valor por pessoa
            if total_pago < valor_por_pessoa:
                falta_pagar = valor_por_pessoa - total_pago
                pessoas_nao_pagaram.append(pessoa)
                self.__tela_viagem.mostra_mensagem(f"- {pessoa.nome} | Falta pagar: R$ {falta_pagar:.2f}")
        
        if not pessoas_nao_pagaram:
            self.__tela_viagem.mostra_mensagem("Todas as pessoas cadastradas pagaram o valor completo do pacote.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.exibir_valor_total,
            2: self.exibir_valor_total_por_pessoa,
            3: self.valor_pago,
            4: self.verificar_quem_pagou,
            5: self.verificar_quem_nao_pagou
        }
        while True:
            opcao = self.__tela_viagem.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
