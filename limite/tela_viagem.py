class TelaViagem():
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
        print('-------Informações da Viagem-------')
        print('0 - Retornar')
        print('1 - Verificar valor total da viagem')
        print('2 - verificar valor total por pessoa')
        print('3 - Verificar quanto já foi pago')
        print('4 - Verificar quem pagou')
        print('5 - Verificar quem não pagou')
        opcao = self.le_num_inteiro('Escolha a opcao: ', [0, 1, 2, 3, 4, 5])
        return opcao

    def mostra_mensagem(self, mensagem):
        print(mensagem)
