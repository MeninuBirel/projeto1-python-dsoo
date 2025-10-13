class TelaEmpresa:
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
        print('-------MENU DE EMPRESAS-------')
        print('0 - Retornar')
        print('1 - Incluir Empresa')
        print('2 - Excluir Empresa')
        print('3 - Alterar Dados da Empresa')
        print('4 - Listar Empresas ')
        opcao = self.le_num_inteiro('Escolha a opcao: ', [0, 1, 2, 3, 4])
        return opcao
    
    def pega_dados_empresa(self):
        print('----- Dados Empresa -----')
        nome = input('Nome: ')
        cnpj = input('CNPJ: ')
        telefone = input('Telefone: ')
        if isinstance(nome, str) and isinstance(cnpj, str) and isinstance(telefone, str):
            return {'nome': nome, 'cnpj': cnpj, 'telefone': telefone}
    
    def mostra_empresa(self, dados_empresa):
        print('Nome: ', dados_empresa['nome'])
        print('Cnpj: ', dados_empresa['cnpj'])
        print('Telefone: ', dados_empresa['telefone'])
        print('\n')

    def mostra_empresas(self, empresa):
        self.mostra_mensagem(str(empresa))  # Usa o __str__ da Entidade
    
    def seleciona_empresa(self):
        cnpj = input('CNPJ da empresa que deseja selecionar: ')
        return cnpj
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)
        
