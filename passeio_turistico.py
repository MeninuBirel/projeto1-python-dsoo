from pessoa import Pessoa

class PasseioTuristico:
    def __init__(self, cidade: str, atracao_turistica: str, horario_inc: int, horario_fim: int, valor_passeio: float, pessoa: Pessoa):
        self.__cidade = None
        self.__atracao_turistica = None
        self.__horario_inc = None
        self.__horario_fim = None
        self.__valor_passeio = None
        self.__pessoas_no_passeio = []
        if isinstance(cidade, str):
            self.__cidade = cidade
        if isinstance(atracao_turistica, str):
            self.__atracao_turistica = atracao_turistica
        if isinstance(horario_inc, int):
            self.__horario_inc = horario_inc
        if isinstance(horario_fim, int):
            self.__horario_fim = horario_fim
        if isinstance(valor_passeio, float):
            self.__valor_passeio = valor_passeio
        

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        if isinstance(cidade, str):
            self.__cidade = cidade


    @property
    def atracao_turistica(self):
        return self.__atracao_turistica

    @atracao_turistica.setter
    def atracao_turistica(self, atracao_turistica: str):
        if isinstance(atracao_turistica, str):
            self.__atracao_turistica = atracao_turistica


    @property
    def horario_inc(self):
        return self.__horario_inc

    @horario_inc.setter
    def horario_inc(self, horario_inc: int):
        if isinstance(horario_inc, int):
            self.__horario_inc = horario_inc


    @property
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim: int):
        if isinstance(horario_fim, int):
            self.__horario_fim = horario_fim


    @property
    def valor_passeio(self):
        return self.__valor_passeio

    @valor_passeio.setter
    def valor_passeio(self, valor_passeio: float):
        if isinstance(valor_passeio, float):
            self.__valor_passeio = valor_passeio


    @property
    def pessoas_no_passeio(self):
        return self.__pessoas_no_passeio

    def incluir_pessoa_no_passeio(self, pessoa: Pessoa):

    def excluir_pessoa_no_passeio(self, pessoa: Pessoa):
