from pessoa import Pessoa
from trecho import Trecho

class CompraPassagem:
    def __init__(self, pessoa_que_comprou: Pessoa):
        self.__pessoa_que_comprou = None
        self.__pessoas_para_quem_comprou = []
        self.__trechos = []
        if isinstance(pessoa_que_comprou, Pessoa):
            self.__pessoa_que_comprou = pessoa_que_comprou
            self.__pessoas_para_quem_comprou.append(pessoa_que_comprou)
    
    @property

    @pessoa_que_comprou.setter

    @property
    def pessoas_para_quem_comprou(self):
        return self.__pessoas_para_quem_comprou
    
    @property
    def trechos(self):
        return self.__trechos
    
    def incluir_pessoa_para_quem_pagou(self, pessoa: Pessoa):
    
    def excluir_pessoa_para_quem_pagou(self, pessoa: Pessoa):

    def incluir_trecho(): #acho que é composição, igual o exemplo do motor
        #adicionar o valor no valor total da viagem
        # multiplica o valor do trecho pela quantidade de pessoas para quem foi comprada esse trecho (len(pessoas_para_quem_comprou)) e adicna no valor total da viagem

        # correr a lista de pessoas do trecho e adiciona o valor indicidual do trecho para o valor_falta_pagar de cada pesoa

    def excluir_trecho():
