class TelaTransporte:
    def menu_transporte(self):
        print("\n----- Gestão de Transportes -----")
        print("1. Cadastrar Transporte")
        print("2. Listar Transportes")
        print("0. Voltar ao Menu anterior")
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                return opcao
            except ValueError:
                print("Opção inválida! Por favor, digite um número.")

    def pega_dados_transporte(self, empresas: list) -> dict:
        print("\n--- Cadastro de Novo Transporte ---")
        print("Selecione a empresa:")
        for i, empresa in enumerate(empresas):
            print(f"{i + 1}. {empresa.nome}")
        while True:
            try:
                escolha = int(input("Número da empresa: "))
                if 1 <= escolha <= len(empresas):
                    empresa_selecionada = empresas[escolha - 1]
                    break
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor, digite um número.")
        tipo = input("Tipo do transporte: ")
        return {
            "empresa": empresa_selecionada,
            "tipo": tipo,
        }

    def mostra_transportes(self, transportes: list):
        print("\n--- Lista de Transportes Cad
