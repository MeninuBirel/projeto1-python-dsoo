class TelaSistema:
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

    def tela_opcoes(self):
        print('----------Sistema de Viagens----------')
        print('Escolha uma opção')
        print('1 - Pessoas')
        print('2 - Locais')
        print('3 - Transporte') # Corrigido 'Transposrte' -> 'Transporte'
        print('4 - Empresas')
        print('5 - Trechos')
        print('6 - Passeios Turísticos')
        print('7 - Realizar Pagamentos')
        print('8 - Valores da Viagem e Informações dos Pagantes')
        print('0 - Finalizar sistema')
        
        opcoes_validas = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        opcao = self.le_num_inteiro('Escolha a opcao: ', opcoes_validas)
        return opcao
