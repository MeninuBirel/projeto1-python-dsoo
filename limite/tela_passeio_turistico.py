class TelaPasseioTuristico():
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

    def le_num_float(self, mensagem: str = 'Digite um valor: ', minimo: float = 0.0):
        while True:
            valor_lido = input(mensagem)
            try:
                # 1. Tenta converter a entrada (string) para float
                valor = float(valor_lido)

                # 2. Verifica se atende a um requisito mínimo (como valor > 0)
                if valor <= minimo:
                    print(f'Valor Incorreto: O valor deve ser maior que {minimo:.2f}.')
                    continue

                # 3. Se tudo estiver correto, retorna o valor
                return valor

            except ValueError:
                # 4. Trata o erro se a conversão para float falhar
                print('Valor Incorreto: Digite um valor numérico válido (ex: 10.50).')

    def mostra_tela_opcoes(self):
        print('-------CADASTRO PASSEIOS-------')
        print('0 - Retornar')
        print('1 - Incluir Passeio Turístico')
        print('2 - Excluir Passeio Turístico')
        print('3 - Listar Passeios Turísticos')
        opcao = self.le_num_inteiro('Escolha a opcao: ', [0, 1, 2, 3]) # Corrigido para incluir a opção 3
        return opcao

    def pega_dados_passeio(self):
        print('----- Dados Passeio -----')
        dia = input('Dia: ')
        cidade = input('Cidade: ')
        atracao_turistica = input('Atração Turística: ')
        horario_inc = input('Horário Início: ')
        horario_fim = input('horário Fim: ')
        valor_passeio = self.le_num_float('Valor Passeio: R$ ', minimo=0.0)
        
        # A validação de tipo já é feita nas funções de leitura.
        # Esta verificação pode ser simplificada ou removida se confiar nas entradas.
        if all(isinstance(val, str) for val in [dia, cidade, atracao_turistica, horario_inc, horario_fim]) \
           and isinstance(valor_passeio, float):
            return {
                'dia': dia,
                'cidade': cidade,
                'atracao_turistica': atracao_turistica,
                'horario_inc': horario_inc,
                'horario_fim': horario_fim,
                'valor_passeio': valor_passeio
            }

    def mostra_passeio(self, dados_passeio):
        print('Dia: ', dados_passeio['dia'])
        print('Cidade: ', dados_passeio['cidade'])
        print('Atração Turística: ', dados_passeio['atracao_turistica'])
        print('Horario Início: ', dados_passeio['horario_inc'])
        print('Horario Fim: ', dados_passeio['horario_fim'])
        print('Valor Passeio: ', dados_passeio['valor_passeio'])
        print('\n')

    def seleciona_passeio(self):
        atracao_turistica = input('Atração Turística do passeio que deseja selecionar: ')
        return atracao_turistica

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_passeios(self, passeio):
        self.mostra_mensagem(str(passeio))  # Usa o __str__ da Entidade
