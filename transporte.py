from .empresa import Empresa

class Transporte:
    def __init__(self, tipo: str, empresa: Empresa, valor: float):
        self.tipo = tipo
        self.empresa = empresa
        self.valor = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, novo_tipo: str):
        if not isinstance(novo_tipo, str) or not novo_tipo.strip():
            raise ValueError("O tipo de transporte deve ser um texto não vazio.")
        self.__tipo = novo_tipo

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, nova_empresa: Empresa):
        if not isinstance(nova_empresa, Empresa):
            raise TypeError("O atributo 'empresa' deve ser uma instância da classe Empresa.")
        self.__empresa = nova_empresa

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor: float):
        if not isinstance(novo_valor, (float, int)):
            raise TypeError("O valor deve ser um número (float ou int).")
        if novo_valor < 0:
            raise ValueError("O valor do transporte não pode ser negativo.")
        self.__valor = float(novo_valor)

    def __str__(self):
        nome_empresa = self.empresa.nome if self.empresa else "N/A"
        return (
            f"Transporte [Tipo: {self.tipo}, Empresa: {nome_empresa}, "
            f"Valor: R$ {self.valor:.2f}]"
        )
