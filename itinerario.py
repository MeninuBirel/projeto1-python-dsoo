from passeio_turistico import PasseioTuristico

class Itinerario:
    def __init__(self, dia: int):
        self.__dia = None
        if isinstance(dia, int):
            self.__dia = dia
        self.__passeios_turisticos = []
    
    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia: int):
        if isinstance(dia, int):
            self.__dia = dia
    
    @property
    def passeios_turisticos(self):
        return self.__passeios_turisticos

    def incluir_passeio(self,cidade: str, atracao_turistica: str, horario_inc: int, horario_fim: int, valor_passeio: float):
        if isinstance(cidade, str) and isinstance(atracao_turistica, str) and isinstance(horario_inc, int) and isinstance(horario_fim, int) and isinstance(valor_passeio, float):
            self.__passeios_turisticos.append(PasseioTuristico(cidade, atracao_turistica, horario_inc, horario_fim, valor_passeio))
        #adicionar valor total na viagem -> multiplica valor do passei pela qnt de pessoa na viagem (nao no passeio)
        #adicionar valor a pagar para a pessoa
    
    def excluir_passeio(self,cidade: str, atracao_turistica: str, horario_inc: int, horario_fim: int, valor_passeio: float):
        if isinstance(cidade, str) and isinstance(atracao_turistica, str) and isinstance(horario_inc, int) and isinstance(horario_fim, int) and isinstance(valor_passeio, float):
            self.__passeios_turisticos.remove(PasseioTuristico(cidade, atracao_turistica, horario_inc, horario_fim, valor_passeio))
        #remover valor do total
        #remover valor a pagar para a pessoa
        pessoa.valor_total_pessoa -= valor_passeio
