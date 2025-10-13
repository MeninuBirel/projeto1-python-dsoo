class TelaTransporte():

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
    
    def mostra_tela_opcoes(self):
        print('-------GESTÃO DE TRANSPORTES-------')
        print('0 - Retornar')
        print('1 - Cadastrar Transporte')
        print('2 - Excluir Trasnporte')
        print('3 - Alterar Transporte')
        print('4 - Listar Transportes')
        opcao = self.le_num_inteiro('Escolha a opcao: ', [0, 1, 2, 3, 4])
        return opcao
    
    def pega_dados_transporte(self):
        print('----- Dados Transporte -----')
        tipo = input('Tipo: ')
        empresa = self.seleciona_empresa()
        if empresa is None:
            return None

        return {
            'tipo': tipo,
            'empresa': empresa,
        }

    def seleciona_empresa(self):
        controlador_empresa = self.__controlador.controlador_empresas
        empresas_cadastradas = controlador_empresa.empresas
        print('\n--- Seleção de Empresa ---')

        if not empresas_cadastradas:
            self.mostra_mensagem("Erro: Não há empresas cadastradas.")
            return None

        opcoes_validas = []
        for i, empresa in enumerate(empresas_cadastradas):
            print(f"{i + 1} - Nome: {empresa.nome} | CNPJ: {empresa.cnpj}")
            opcoes_validas.append(i + 1)

        opcoes_validas.append(0)  # Opção para Cancelar
        while True:
            escolha = self.le_num_inteiro(
                "Selecione o número da empresa (0 para cancelar): ", opcoes_validas
            )
            if escolha == 0:
                self.mostra_mensagem("Operação cancelada.")
                return None
            # Retorna o OBJETO empresa selecionado
            return empresas_cadastradas[escolha - 1]

    def seleciona_transporte(self):
        tipo = input('Tipo do Transporte: ')
        #selecionar empresa
        controlador_empresa = self.__controlador.controlador_empresas
        empresas_cadastradas = controlador_empresa.empresas
        if not empresas_cadastradas:
            self.mostra_mensagem("Erro: Não há empresas cadastradas para referência.")
            return None
        self.mostra_mensagem("\n--- Empresas Cadastradas ---")
        for empresa in empresas_cadastradas:
            print(f"Nome: {empresa.nome} | CNPJ: {empresa.cnpj}")
        self.mostra_mensagem("--------------------------")
        cnpj = input('CNPJ da Empresa do Transporte: ')
        
        if isinstance(tipo, str) and isinstance(cnpj, str):
            return {'tipo': tipo, 'cnpj': cnpj}
        else:
             self.mostra_mensagem("Erro na entrada de dados.")
             return None

    def mostra_transporte(self, dados_transporte):
        nome_empresa = dados_transporte['empresa'].nome if dados_transporte['empresa'] else "N/A"
        print('Tipo: ', dados_transporte['tipo'])
        print('Empresa: ', nome_empresa) 
        print('\n')
    
    def mostra_transportes(self, transporte):
        self.mostra_mensagem(str(transporte))  
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)
