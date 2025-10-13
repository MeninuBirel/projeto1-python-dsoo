from entidade.empresa import Empresa

class Transporte():
    def __init__(self, tipo: str, empresa: Empresa):
        self.__tipo = None
        if isinstance(tipo, str):
            self.__tipo = tipo
        self.__empresa = None
        if isinstance(empresa, Empresa):
            self.__empresa = empresa
            
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: str):
        if not isinstance(tipo, str) or not tipo.strip():
            raise ValueError("O tipo de transporte deve ser um texto não vazio.")
        self.__tipo = tipo
        
    @property
    def empresa(self):
        return self.__empresa
    
    @empresa.setter
    def empresa(self, empresa: Empresa):
        if not isinstance(empresa, Empresa):
            raise TypeError("O atributo 'empresa' deve ser uma instância da classe Empresa.")
        self.__empresa = empresa
        
    def __str__(self):
        nome_empresa = self.empresa.nome if self.empresa else "N/A"
        return (
            f"Transporte - Tipo: {self.tipo}, Empresa: {nome_empresa}, "
        )
