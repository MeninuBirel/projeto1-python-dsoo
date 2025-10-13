from entidade.pagamento import Pagamento
from entidade.pessoa import Pessoa

class Pix(Pagamento):
    def __init__(self, valor: float, pessoa: Pessoa, data: str, cpf: str):
        super().__init__(valor, pessoa, data)
        self.__cpf = None
        if isinstance(cpf, str):
            self.__cpf = cpf
 
    @property
    def cpf(self):
        return self.__cpf
        
    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf
        else:
            raise ValueError("CPF deve ser uma string não vazia.")
            
    def get_metodo(self):
        return "PIX"

    def __str__(self):
        return f"PIX - Valor: R$ {self.valor:.2f} | Pessoa: {self.pessoa.nome} | Data: {self.data} | CPF: {self.cpf}"
        
