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

    def mostra_tela_opcoes(self):
        print('-------CADASTRO PESSOAS-------')
        print('0 - Retornar')
        print('1 - Incluir Pessoa')
        print('2 - Excluir Pessoa')
        print('3 - Editar dados da Pessoa')
        print('4 - Listar Pessoas')
        opcao = self.le_num_inteiro('Escolha a opcao: ', [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_pessoa(self):
        print('----- Dados Pessoa -----')
        nome = input('Nome: ')
        celular = input('Celular: ')
        identificacao = input('Identificacao: ')
        idade = int(input('idade: '))
        if isinstance(nome, str) and isinstance(celular, str) and isinstance(identificacao, str):
            if idade >= 18:
                return {'nome': nome, 'celular': celular, 'identificacao': identificacao, 'idade': idade}
            else:
                self.mostra_mensagem('Infelizmente menores de idade não podem participar da viagem')

    def mostra_pessoa(self, dados_pessoa):
        print('Nome: ', dados_pessoa['nome'])
        print('Celular: ', dados_pessoa['celular'])
        print('identificacao: ', dados_pessoa['identificacao'])
        print('Idade: ', dados_pessoa['idade'])
        print('\n')

    def seleciona_pessoa(self):
        identificacao = input('Identificação da pessoa que deseja selecionar: ')
        return identificacao

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_pessoas(self, pessoa):
        self.mostra_mensagem(str(pessoa))
