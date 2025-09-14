class Dinheiro(Pagamento):

    def __init__(self, valor: float, pessoa: Pessoa, data: str, cpf: str):
        super().__init__(valor, pessoa, data)
        self.__cpf = None
        if isinstance(cpf, str):
            self.__cpf = cpf
        
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf
            
    #?????????
    def executar_pagamento():
        pessoa.valor_falta_pagar -= valor
        pessoa.valor_pago += valor
        valor_pago += valor #da viagem total
