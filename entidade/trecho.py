from entidade.transporte import Transporte
from entidade.local import Local

class Trecho:
    def __init__(self, data: str, origem: Local,
                 destino: Local, transporte: Transporte, valor_trecho: float):
        self.__data = None
        if isinstance(data, str):
            self.__data = data
        self.__origem = None
        if isinstance(origem, Local):
            self.__origem = origem
        self.__destino = None
        if isinstance(destino, Local):
            self.__destino = destino
        self.__transporte = None
        if isinstance(transporte, Transporte):
            self.__transporte = transporte
        self.__valor_trecho = None
        if isinstance(valor_trecho, float):
            self.__valor_trecho = valor_trecho


    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: str):
        if isinstance(data, str):
            self.__data = data
    
    @property
    def origem(self):
        return self.__origem
    
    @origem.setter
    def origem(self, origem: Local):
        if isinstance(origem, Local):
            self.__origem = origem
    
    @property
    def destino(self):
        return self.__destino
    
    @destino.setter
    def destino(self, destino: Local):
        if isinstance(destino, Local):
            self.__destino = destino

    @property
    def transporte(self):
        return self.__transporte
    
    @transporte.setter
    def transporte(self, transporte: Transporte):
        if isinstance(transporte, Transporte):
            self.__transporte = transporte

    @property
    def valor_trecho(self):
        return self.__valor_trecho

    @valor_trecho.setter
    def valor_trecho(self, valor_trecho: float):
        if isinstance(valor_trecho, float):
            self.__valor_trecho = valor_trecho # O erro de usar 'self.valor_trecho' em vez de '__valor_trecho' foi mantido, pois não é permitido alterar o código.
            
    def __str__(self):
        return f"Trecho - Data: {self.__data} | Origem: {self.__origem} | Destino: {self.__destino} | Transporte: {self.__transporte} | valor: {self.__valor_trecho}"
        
