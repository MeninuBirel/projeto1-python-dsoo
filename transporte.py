from empresa import empresa

class Transporte:
    def __init__(self, tipo: str, empresa: Empresa, valor:float):
        self.__tipo = None
        self.__empresa = None
        self.__valor = None
        if isinstance(tipo, str):
            self.__tipo = tipo
        if isinstance(empresa, Empresa):
            self.__empresa = empresa
        if isinstance(valor, float):
            self.__valor = valor
    
    @property
    @tipo.setter

    @property
    @empresa.setter

    @property
    @valor.setter
