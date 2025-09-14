class cartao(Pagamento):

    def __init__(self, valor: float, pessoa: Pessoa, data: str, numero_cartao: str, bandeira: str):
        super().__init__(valor, pessoa, data)
        self.__numero_cartao = None
        self._-bandeira = None
        if isinstance(numero_cartao, str):
            self.__numero_cartao = numero_cartao
        if isinstance(bandeira, str):
            self.__bandeira = bandeira
        
    @property
    def numero_cartao(self):
        return self.__numero_cartao
    
    @cpf.setter
    def numero_cartao(self, numero_cartao: str):
        if isinstance(numero_cartao, str):
            self.__numero_cartao = numero_cartao
    

    @property
    def bandeira(self):
        return self.__bandeira
    
    @cpf.setter
    def bandeira(self, bandeira: str):
        if isinstance(bandeira, str):
            self.__bandeira = bandeira


    #?????????
    def executar_pagamento():
        pessoa.valor_falta_pagar -= valor
        pessoa.valor_pago += valor
        valor_pago += valor #da viagem total
