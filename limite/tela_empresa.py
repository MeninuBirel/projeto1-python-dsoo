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
        nome = input('Nome: ').capitalize()
        cnpj = self.verificar_se_e_inteiro('cnpj: ', minimo=0)
        telefone = self.verificar_se_e_inteiro('Telefone: ', minimo=0)
        if isinstance(nome, str) and isinstance(cnpj, int) and isinstance(telefone, int):
            return {'nome': nome, 'cnpj': cnpj, 'telefone': telefone}

    def mostra_empresas(self, empresa):
        self.mostra_mensagem(str(empresa))  # Usa o __str__ da Entidade
    
    def seleciona_empresa(self):
        cnpj = self.verificar_se_e_inteiro('CNPJ da empresa que deseja selecionar: ', minimo=0)
        return cnpj
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)
        

        
