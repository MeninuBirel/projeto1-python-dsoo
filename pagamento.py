from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def __init__(self, valor: float, pessoa: Pessoa, data: str):
        self.__valor = None
        self.__pessoa = None
        self.__data = None
        if isinstance(valor, float):
            self.__valor = valor
        if isinstance(pessoa, Pessoa):
            self.__pessoa = pessoa
        if isinstance(data, str):
            self.__data = data
    
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor: float):
        if isinstance(valor, float):
            self.__valor = valor
    
    @property
    def pessoa(self):
        return self.__pessoa
    @pessoa.setter
    def pessoa(self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa):
            self.__pessoa = pessoa

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: str):
        if isinstance(data, str):
            self.__data = data

    @abstractmethod
    def executar_pagamento(self):
        pass
      
