class TelaPessoa():
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
                print('Valor Incorreto: Digite um valor numerico inteiro valido')
                if inteiros_validos:
                    print(f'Valores válidos: {inteiros_validos}')
    
    def verificar_se_e_inteiro(self,  mensagem: str = 'Digite um valor: ', minimo: int = 0):
        while True:
            valor_lido = input(mensagem)
            try:
                valor = int(valor_lido)
                if valor <= minimo:
                    print(f'Número Incorreto: O valor deve ser maior que {minimo}.')
                    continue
                return valor
            except ValueError:
                print('Número Incorreto: Digite um valor numérico válido - números inteiros.')
    
    def seleciona_qual_viagem(self):
        controlador_viagem = self.__controlador.controlador_sistema.controlador_viagens  #como fazer essa parte?????? sem dar tanta moral para a tela
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
        print('-------CADASTRO PESSOAS-------')
        print('0 - Retornar')
        print('1 - Incluir Pessoa')
        print('2 - Excluir Pessoa de uma Viagem')
        print('3 - Excluir Pessoa do Sistema')
        print('4 - Editar dados da Pessoa')
        print('5 - Listar Pessoas de uma Viagem')
        print('6 - Listar Pessoas do Sistema')
        opcao = self.le_num_inteiro('Escolha a opcao: ', [0, 1, 2, 3, 4, 5, 6])
        return opcao
    
    def pega_dados_pessoa(self):
        print('----- Dados Pessoa -----')
        nome = input('Nome: ').capitalize()
        celular = self.verificar_se_e_inteiro('celular: ', minimo=0)
        identificacao = self.verificar_se_e_inteiro('identificacao: ', minimo=0)
        idade = self.verificar_se_e_inteiro('idade: ', minimo=17)
        if isinstance(nome, str) and isinstance(celular, int) and isinstance(identificacao, int) and isinstance(idade, int):
            return {'nome': nome, 'celular': celular, 'identificacao': identificacao, 'idade': idade}

    def mostra_pessoas(self, pessoa):
        self.mostra_mensagem(str(pessoa))
    
    def seleciona_pessoa(self):
        identificacao = self.verificar_se_e_inteiro('Identificação da pessoa que deseja selecionar: ', minimo=0)
        return identificacao
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)
