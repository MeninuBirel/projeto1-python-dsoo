class Empresa:
    def __init__(self, nome: str, cnpj: str, telefone: str):
        self._nome = nome
        self._cnpj = self._formatar_cnpj(cnpj)
        self._telefone = telefone
        self.transportes = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("Digite um nome válido")
        self._nome = novo_nome

    @property
    def cnpj(self):
        return (
            f"{self._cnpj[:2]}.{self._cnpj[2:5]}.{self._cnpj[5:8]}/"
            f"{self._cnpj[8:12]}-{self._cnpj[12:]}"
        )

    @cnpj.setter
    def cnpj(self, novo_cnpj: str):
        self._cnpj = self._formatar_cnpj(novo_cnpj)

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone: str):
        if not isinstance(novo_telefone, str) or not novo_telefone.strip():
            raise ValueError("Digite um telefone válido")
        self._telefone = novo_telefone

    def adicionar_transporte(self, transporte):
        self.transportes.append(transporte)

    def _formatar_cnpj(self, cnpj: str):
        if not isinstance(cnpj, str):
            raise TypeError("Digite um CNPJ válido")
        cnpj_limpo = "".join(filter(str.isdigit, cnpj))

        if len(cnpj_limpo) != 14:
            raise ValueError("O CNPJ deve conter 14 dígitos.")
        return cnpj_limpo

    def __str__(self):
        return f"Empresa: {self.nome} | CNPJ: {self.cnpj} | Telefone: {self.telefone}"
