class Empresa():
    def __init__(self, nome: str, cnpj: str, telefone: str):
        self.__nome = None
        if isinstance(nome, str):
            self.__nome = nome
        self.__cnpj = None
        if isinstance(cnpj, str):
            self.__cnpj = cnpj
        self.__telefone = None
        if isinstance(telefone, str):
            self.__telefone = telefone
        self.__transportes = []
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        
    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        if isinstance(cnpj, str):
            self.__cnpj = cnpj
        
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self._telefone = telefone
        
    def adicionar_transporte(self, transporte):
        self.__transportes.append(transporte)
        
    def _formatar_cnpj(self, cnpj: str):
        if not isinstance(cnpj, str):
            raise TypeError("Digite um CNPJ válido")
        cnpj_limpo = "".join(filter(str.isdigit, cnpj))
        if len(cnpj_limpo) != 14:
            raise ValueError("O CNPJ deve conter 14 dígitos.")
        return cnpj_limpo
    
    def __str__(self):
        return f"Empresa: {self.nome} | CNPJ: {self.cnpj} | Telefone: {self.telefone}"
