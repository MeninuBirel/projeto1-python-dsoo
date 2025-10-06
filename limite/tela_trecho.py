from entidade.trecho import Trecho
from entidade.transporte import Transporte


class TelaTrecho():
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
        print('-------CADASTRO TRECHOS-------')
        print('0 - Retornar')
        print('1 - Incluir Trecho')
        print('2 - Listar Trechos')
        opcao = self.le_num_inteiro('Escolha a opcao: ', [0, 1, 2])
        return opcao

    def seleciona_transporte(self):
        controlador_transportes = self.__controlador.controlador_transportes
        transportes_cadastrados = controlador_transportes.transportes
        print('\n--- Seleção de Transporte ---')

        if not transportes_cadastrados:
            self.mostra_mensagem("Erro: Não há transportes cadastrados.")
            return None

        opcoes_validas = []
        for i, transporte in enumerate(transportes_cadastrados):
            print(f"{i + 1} - Tipo: {transporte.tipo} | Modelo: {transporte.modelo}")
            opcoes_validas.append(i + 1)

        opcoes_validas.append(0)  # Opção para Cancelar
        while True:
            escolha = self.le_num_inteiro(
                "Selecione o número do transporte (0 para cancelar): ", opcoes_validas
            )
            if escolha == 0:
                self.mostra_mensagem("Operação cancelada.")
                return None
            # Retorna o OBJETO Transporte selecionado
            return transportes_cadastrados[escolha - 1]

    def pega_dados_trecho(self):
        print('----- Dados Trecho -----')
        data = input('Data: ')
        cidade_origem = input('Cidade origem: ')
        pais_origem = input('País origem:')
        cidade_destino = input('Cidade destino: ')
        pais_destino = input('País destino: ')
        transporte = self.seleciona_transporte()
        
        # Nota: O código original usava 'transporte_selecionado' aqui, 
        # mas a variável é 'transporte'. Mantive a lógica original.
        if transporte is None:
            return None
            
        valor_trecho = self.le_num_float('Valor Trecho: R$ ', minimo=0.0)

        return {
            'data': data,
            'cidade_origem': cidade_origem,
            'pais_origem': pais_origem,
            'cidade_destino': cidade_destino,
            'pais_destino': pais_destino,
            'transporte': transporte,
            'valor_trecho': valor_trecho
        }

    def mostra_trechos(self, trecho):
        self.mostra_mensagem(str(trecho))  # Usa o __str__ da Entidade

    def mostra_mensagem(self, mensagem):
        print(mensagem)
