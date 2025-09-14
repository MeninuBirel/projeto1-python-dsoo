from local import Local
from passeio_turistico import PasseioTuristico
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
        self.__passeios_turisticos = []
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
    def passeios_turisticos(self):
        return self.__passeios_turisticos
    
    @property
    def quem_pagou(self):
        return self.__quem_pagou
    
    @property
    def quem_nao_pagou(self):
        return self.__quem_nao_pagou

    def incluir_local(self, cidade: str, pais: str, valor: float):
        if isinstance(cidade, str) and isinstance(pais, str) and isinstance(valor, float):
            cidade_existente = self.find_local_by_cidade(cidade)
            if cidade_existente is None: 
                self.__locais.append(Local(cidade, pais, valor))
        
    def excluir_local(self, cidade: str):
        if isinstance(cidade, str):
            cidade_a_remover = self.find_local_by_cidade(cidade)
            if cidade_a_remover:
                self.__locais.remove(cidade_a_remover)
        
    def find_local_by_cidade(self, cidade: str):
        for local in self.__locais:
            if local.cidade == cidade:
                return local
    

    def incluir_pessoa(self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa):
            if pessoa not in self.__pessoas:
                self.__pessoas.append(pessoa)
    
    def excluir_pessoa(self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa):
            if pessoa in self.__pessoas:
                self.__pessoas.remove(pessoa)


    def incluir_passeio(self, dia: str, cidade: str, atracao_turistica: str, horario_inc: int, horario_fim: int, valor_passeio: float):
        if isinstance(dia, str) and isinstance(cidade, str) and isinstance(atracao_turistica, str) and isinstance(horario_inc, int) and isinstance(horario_fim, int) and isinstance(valor_passeio, float):
            passeio_existente = self.find_passeio_by_atracao(atracao_turistica)
            if passeio_existente is None:
                self.__passeios_turisticos.append(PasseioTuristico(dia, cidade, atracao_turistica, horario_inc, horario_fim, valor_passeio))
        #adicionar valor total na viagem -> multiplica valor do passei pela qnt de pessoa na viagem (nao no passeio)
        #adicionar valor a pagar para a pessoa
    
    def excluir_passeio(self, atracao_turistica: str):
        if isinstance(atracao_turistica, sttr):
            passeio_a_remover = self.find_passeio_by_atracao(atracao_turistica)
            if passeio_a_remover:
                self.__passeios_turisticos.remove(passeio_a_remover)
        #remover o valor do passeio do valor toral da viagem
        #remover por pessoa também
    
    def find_passeio_by_atracao(self, atracao_turistica: str):
        for passeio in self.__passeios_turisticos:
            if passeio.atracao_turistica == atracao_turistica:
                return passeio


    def valor_total(self):
    
    def valor_pago(self):

    def verificar_quem_pagou(self):
        #correr a lista das pesoas e if valor == 0 adiciona na lista que já paou do contrario na lista que não pagou
        for viajante in self.__pessoas:
            if viajante.valor_falta_pagar == 0:
                self.__quem_pagou.append(viajante)
            else: 
                self.__quem_nao_pagou.append(viajante)
