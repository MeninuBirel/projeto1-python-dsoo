from transporte import Transporte

class Trecho:
    def __init__(self, data: str, cidade_origem: str, pais_origem: str, cidade_destino: str, pais_destino: str, transporte: Transporte):
        self.__data = None
        self.__origem = None
        if isinstance(cidade_origem, str) and isinstance(pais_origem, str):
            self.__origem = Local(cidade_origem, pais_origem)
        self.__destino = None
        if isinstance(cidade_destino, str) and isinstance(pais_destino, str):
            self.__destino = Local(cidade_destino, pais_destino)
        self.__transporte = None
        if isinstance(transporte, Transporte):
            self.__transporte = transporte
    

    def valor_trecho(self):
        #valor trasnporte + valor cidade(Local) de destino
    
    def pago_ou_naopago(self):
