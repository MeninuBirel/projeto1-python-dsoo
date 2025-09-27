class TelaEmpresa:
    def menu_empresa(self) -> int:
        print("\n----- Menu de Empresas -----")
        print("1. Cadastrar Empresa")
        print("2. Listar Empresas")
        print("3. Ver Detalhes de Empresa e seus Transportes")
        print("0. Voltar ao Menu anterior")

        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                return opcao
            except ValueError:
                print("Opção inválida! Por favor, digite um número.")

    def pega_dados_empresa(self):
        print("\n--- Cadastro de Nova Empresa ---")
        nome = input("Nome: ")
        cnpj = input("CNPJ: ")
        telefone = input("Telefone: ")
        return {"nome": nome, "cnpj": cnpj, "telefone": telefone}

    def mostra_empresas(self, empresas: list):
        print("\n--- Lista de Empresas Cadastradas ---")
        if not empresas:
            print("Nenhuma empresa cadastrada.")
        else:
            for i, empresa in enumerate(empresas, 1):
                print(f"{i}. {empresa.nome}")

    def seleciona_empresa(self, empresas: list):
        self.mostra_empresas(empresas)
        if not empresas:
            return None

        while True:
            try:
                escolha = int(input("Digite o número da empresa para ver os detalhes: "))
                if 1 <= escolha <= len(empresas):
                    return empresas[escolha - 1]
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor, digite um número.")

    def mostra_detalhes_empresa(self, empresa):
        print("\n------ Detalhes da Empresa ------")
        print(f"Nome: {empresa.nome}")
        print(f"CNPJ: {empresa.cnpj}")
        print(f"Telefone: {empresa.telefone}")
        print("--- Transportes Associados ---")
        if not empresa.transportes:
            print("Nenhum transporte cadastrado para esta empresa.")
        else:
            for transporte in empresa.transportes:
                print(f"  - {transporte}")
        print("-------------------------------")

    def mostra_mensagem(self, msg: str):
        print(f"\n>> {msg} <<")
