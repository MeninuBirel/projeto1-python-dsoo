from local import Local
from passeio_turistico import PasseioTuristico
from itinerario import Itinerario
from pessoa import Pessoa

class Viagem:

    def __init__(self, data_inc: str, data_fim: str):
        self.__data_inc = None
        self.__data_fim = None
        if isinstance(data_inc, str):
            self.__data_inc = data_inc
        if isinstance(data_fim, str):
            self.__data_fim = data_fim
        self.__locais = []
        self.__pessoas = []
        self.__itinerarios = []
        self.__quem_pagou = []
        self.__quem_nao_pagou = []

    @property
    def data_inc(self):
        return self.__data_inc

    @data_inc.setter
    def data_inc(self, data_inc: str):
        if isinstance(data_inc, str):
            self.__data_inc = data_inc


    @property
    def data_fim(self):
        return self.__data_fim

    @data_fim.setter
    def data_fim(self, data_fim: str):
        if isinstance(data_fim, str):
            self.__data_fim = data_fim
    
    @property
    def locais(self):
        return self.__locais

    @property
    def pessoas(self):
        return self.__pessoas

    @property
    def itinerarios(self):
        return self.__itinerarios
    
    @property
    def quem_pagou(self):
        return self.__quem_pagou
    
    @property
    def quem_nao_pagou(self):
        return self.__quem_nao_pagou

    
    def incluir_local(self, local: Local):
        

    def excluir_local(self, local: Local):
        

    
    def incluir_pessoa(self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa):
            if pessoa not in self.__pessoas:
                self.__pessoas.append(pessoa)
    
    def excluir_pessoa(self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa):
            if pessoa in self.__pessoas:
                self.__pessoas.remove(pessoa)
    
    def incluir_itinerario(self, dia: int):
    

    def excluir_itinerario(self, dia: int):


    def valor_total(self):

    
    def valor_pago(self):

    def verificar_quem_pagou(self):
        #correr a lista das pesoas e if valor == 0 adiciona na lista que já paou do contrario na lista que não pagou
