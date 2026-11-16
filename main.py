def exibirMenuPrincipal():
    print("\n---------- Sistema de RH ----------")
    print("1 - Cadastrar Estagiário")
    print("2 - Cadastrar Desenvolvedor")
    print("3 - Cadastrar Gerente")
    print("4 - Listar funcionários")
    print("5 - Consultar funcionário por ID")
    print("0 - Encerrar sistema")

def executarOpcao(opcao):
    if opcao == "0":
        return True
    else:
        exibirOpcaoInvalida()
    return False

def lerString(mensagem):
    return input(mensagem)

def lerInt(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("\n--- Insira um valor válido! ---")

def lerFloat(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("\n--- Insira um valor válido! ---")

def exibirOpcaoInvalida():
    print("\n--- Insira uma opcao válida! ---")

while True:
    exibirMenuPrincipal()
    opcao = input("\nInsira a opção desejada: ")
    if executarOpcao(opcao):
        break