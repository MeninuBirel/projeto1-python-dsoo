class TelaLocal():
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
        print('-------CADASTRO LOCAIS-------')
        print('0 - Retornar')
        print('1 - Incluir Local')
        print('2 - Excluir Local')
        print('3 - Listar Locais')

        opcao = self.le_num_inteiro('Escolha a opcao: ', [0, 1, 2, 3])
        return opcao

    def pega_dados_local(self):
        print('----- Dados Local -----')
        cidade = input('Cidade: ')
        pais = input('País: ')
        if isinstance(cidade, str) and isinstance(pais, str):
            return {'cidade': cidade, 'pais': pais}

    def mostra_local(self, dados_local):
        print('Cidade: ', dados_local['cidade'])
        print('Pais: ', dados_local['pais'])
        print('\n')

    def seleciona_local(self):
        cidade = input('Cidade do local que deseja selecionar: ')
        return cidade

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_locais(self, local):
        self.mostra_mensagem(str(local))  # Usa o __str__ da Entidade
