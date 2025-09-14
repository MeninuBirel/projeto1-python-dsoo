class Local:
    def __init__(self, cidade: str, pais: str, valor: float):
        self.__cidade = None
        self.__pais = None
        self.__valor = None
        if isinstance(cidade, str):
            self.__cidade = cidade
        if isinstance(pais, str):
            self.__pais = pais
        if isinstance(valor, float):
            self.__valor = valor

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        if isinstance(cidade, str):
            self.__cidade = cidade


    @property
    def pais(self):
        return self.__pais
        
    @pais.setter
    def pais(self, pais: str):
        if isinstance(pais, str):
            self.__pais = pais
    
    @property
    def valor(self):
        return self.__valor
    
    @valor_setter
    def valor(self, valor: float):
        if isinstance(valor, float):
            self.__valor = valor
