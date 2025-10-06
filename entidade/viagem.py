class Viagem():
    def __init__(self, data_fim: str, data_inc: str):
        self.__data_inc = None
        if isinstance(data_inc, str):
            self.__data_inc = data_inc
        self.__data_fim = None
        if isinstance(data_fim, str):
            self.__data_fim = data_fim

    @property
    def data_inc(self):
        return self.__data_inc

    @data_inc.setter
    def data_inc(self, data_inc):
        if isinstance(data_inc, str):
            self.__data_inc = data_inc

    @property
    def data_fim(self):
        return self.__data_fim

    @data_fim.setter
    def data_fim(self, data_fim):
        if isinstance(data_fim, str):
            self.__data_fim = data_fim
