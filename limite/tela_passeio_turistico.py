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

    def verificar_se_e_float(self, mensagem: str = 'Digite um valor: ', minimo: float = 0.0):
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
        print('-------CADASTRO PASSEIOS-------')
        print('0 - Retornar')
        print('1 - Incluir Passeio Turístico')
        print('2 - Excluir Passeio Turístico')
        print('3 - Alterar Passeio Turístico')
        print('4 - Listar Passeios Turísticos de uma Viagem')
        opcao = self.le_num_inteiro('Escolha a opcao: ', [0, 1, 2, 3, 4])
        return opcao
    
    def pega_dados_passeio(self):
        print('----- Dados Passeio -----')
        dia = input('Dia: ')
        cidade = input('Cidade: ').capitalize()
        atracao_turistica = input('Atração Turística: ').capitalize()
        horario_inc = input('Horário Início: ')
        horario_fim = input('horário Fim: ')
        valor_passeio = self.verificar_se_e_float('Valor Passeio: R$ ', minimo=0.0) 
        if isinstance(dia, str) and isinstance(cidade, str) and isinstance(atracao_turistica, str) and isinstance(horario_inc, str) and isinstance(horario_fim, str) and isinstance(valor_passeio, float):
            return {
                'dia': dia,
                'cidade': cidade,
                'atracao_turistica': atracao_turistica,
                'horario_inc': horario_inc,
                'horario_fim': horario_fim,
                'valor_passeio': valor_passeio
            }
    
    def seleciona_passeio(self):
        atracao_turistica = input('Atração Turística do passeio que deseja selecionar: ').capitalize()
        return atracao_turistica

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_passeios(self, passeio):
        self.mostra_mensagem(str(passeio))
