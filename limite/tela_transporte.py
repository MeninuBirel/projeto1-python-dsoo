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
        tipo.capitalize()
        return {'tipo': tipo}

    def seleciona_transporte(self):
        tipo = input('Tipo do Transporte: ')
        tipo.capitalize()
        if isinstance(tipo, str):
            return tipo
        else:
             self.mostra_mensagem("Erro na entrada de dados.")
             return None

    def mostra_transportes(self, transporte):
        self.mostra_mensagem(str(transporte))  
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)
