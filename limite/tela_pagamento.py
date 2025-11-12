class TelaPagamento():
    def __init__(self, controlador):
        self.__controlador = controlador

    def le_num_inteiro(self, mensagem: str = '', inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print('Valor Incorreto: Digite um valor numérico inteiro válido')
                if inteiros_validos:
                    print(f'Valores válidos: {inteiros_validos}')
    
    def seleciona_qual_viagem(self):
        controlador_viagem = self.__controlador.controlador_sistema.controlador_viagens #como fazer essa parte?????? sem dar tanta moral para a tela
        viagens_cadastradas = controlador_viagem.viagens
        print('\n--- Seleção da Viagem ---')

        if not viagens_cadastradas:
            self.mostra_mensagem("Erro: Não há viagens cadastradas.")
            return None

        opcoes_validas = []
        for i, viagem in enumerate(viagens_cadastradas):
            print(f"{i + 1} - Código: {viagem.codigo} | Nome: {viagem.nome_viagem} | Início: {viagem.data_inc} | Fim: {viagem.data_fim}")
            opcoes_validas.append(i + 1)

        opcoes_validas.append(0)  # Opção para Cancelar
        while True:
            escolha = self.le_num_inteiro(
                "Selecione o número da viagem (0 para cancelar): ", opcoes_validas
            )
            if escolha == 0:
                self.mostra_mensagem("Operação cancelada.")
                return None
            # Retorna o OBJETO viagem selecionado
            return viagens_cadastradas[escolha - 1]
    
    def mostra_tela_opcoes(self):
        print('-------GESTÃO DE PAGAMENTOS-------')
        print('1 - Registrar Novo Pagamento')
        print('2 - Listar Pagamentos')
        print('0 - Retornar')
        opcao = self.le_num_inteiro('Escolha a opção: ', [0, 1, 2])
        return opcao
    
    def seleciona_pessoa_pagamento(self, pessoas: list):
        print('\n--- Seleção do Pagador ---')
        if not pessoas:
            self.mostra_mensagem("Erro: Não há pessoas cadastradas para realizar o pagamento.")
            return None
        for i, pessoa in enumerate(pessoas):
            print(f"{i+1} - Nome: {pessoa.nome} | ID: {pessoa.identificacao}")

        while True:
            try:
                opcoes_validas = [i + 1 for i in range(len(pessoas))] + [0]
                escolha = self.le_num_inteiro("Selecione o número do pagador (0 para cancelar): ", opcoes_validas)
                
                if escolha == 0:
                    return None
                
                return pessoas[escolha - 1]
            except Exception:
                self.mostra_mensagem("Opção inválida.")
    
    def pega_dados_pagamento(self, pessoa_selecionada):
        print(f"\n----- Dados Pagamento para {pessoa_selecionada.nome} -----")
        data = input('Data (DD/MM/AAAA): ')

        while True:
            try:
                valor = float(input('Valor do Pagamento: R$ '))
                if valor <= 0:
                    raise ValueError
                break
            except ValueError:
                self.mostra_mensagem("Valor inválido. Digite um número positivo.")
        
        # Apresenta o menu de escolha ao usuário.
        print('\n--- Escolha o Método de Pagamento ---')
        print('1 - PIX')
        print('2 - DINHERO')
        print('3 - CARTÃO')

        metodo = self.le_num_inteiro('Escolha o método: ', [1, 2, 3])

        # Inicializa um dicionário com as informações compartilhadas.
        dados = {'valor': valor, 'data': data, 'pessoa': pessoa_selecionada}

        # Se for PIX, adiciona a chave 'tipo' e coleta o CPF.
        if metodo == 1:
            dados['tipo'] = 'PIX'
            dados['cpf'] = pessoa_selecionada.identificacao
        elif metodo == 2:
            dados['tipo'] = 'DINHEIRO'
            dados['cpf'] = pessoa_selecionada.identificacao
        # Se for CARTÃO, adiciona o 'tipo' e coleta os dados específicos.
        elif metodo == 3:
            dados['tipo'] = 'CARTAO'
            dados['numero_cartao'] = input('Número do Cartão: ')
            dados['bandeira'] = input('Bandeira (Visa, Master, etc.): ')
        return dados

    def mostra_pagamento(self, pagamento):
        self.mostra_mensagem(str(pagamento))  # Usa o __str__ da Entidade

    def mostra_mensagem(self, mensagem):
        print(mensagem)

