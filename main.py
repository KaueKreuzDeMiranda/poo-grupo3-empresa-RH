from model.Desenvolvedor import Desenvolvedor
from model.Estagiario import Estagiario
from model.Gerente import Gerente

funcionarios = []

def exibirMenuPrincipal():
    print("\n---------- Sistema de RH ----------")
    print("1 - Cadastrar Estagiário")
    print("2 - Cadastrar Desenvolvedor")
    print("3 - Cadastrar Gerente")
    print("0 - Encerrar sistema")

def executarOpcao(opcao):
    if opcao == "1":
        cadastrarEstagiario()
    elif opcao == "2":
        cadastrarDesenvolvedor()
    elif opcao == "3":
        cadastrarGerente()
    elif opcao == "0":
        return True
    else:
        exibirOpcaoInvalida()
    return False

def cadastrarEstagiario():
    print("\n--- Cadastro de estagiário ---")
    identificador = lerInt("\nInsira o identificador do estagiário: ")
    nome = lerString("\nInsira o nome do estagiário: ")
    idade = lerInt("\nInsira a idade do estagiário: ")
    salario = lerFloat("\nInsira o salário do estagiário: ")
    curso = lerString("\nInsira o curso do estagiário: ")
    tutor = lerString("\nInsira o tutor do estagiário: ")

    estagiario = Estagiario(identificador, nome, idade, salario, curso, tutor)
    registrarFuncionario(estagiario)

def cadastrarDesenvolvedor():
    print("\n--- Cadastro de desenvolvedor ---")
    identificador = lerInt("\nInsira o identificador do desenvolvedor: ")
    nome = lerString("\nInsira o nome do desenvolvedor: ")
    idade = lerInt("\nInsira a idade do desenvolvedor: ")
    salario = lerFloat("\nInsira o salário do desenvolvedor: ")
    nivel = lerString("\nInsira o nível de senioridade do desenvolvedor: ")
    stack = lerString("\nInsira em qual stack trabalha o desenvolvedor: ")

    desenvolvedor = Desenvolvedor(identificador, nome, idade, salario, nivel, stack)
    registrarFuncionario(desenvolvedor)

def cadastrarGerente():
    print("\n--- Cadastro de gerente ---")
    identificador = lerInt("\nInsira o identificador do gerente: ")
    nome = lerString("\nInsira o nome do gerente: ")
    idade = lerInt("\nInsira a idade do gerente: ")
    salario = lerFloat("\nInsira o salário do gerente: ")
    departamento = lerString("\nInsira o departamento de gerência do gerente: ")
    tamanho_equipe = lerInt("\nInsira o tamanho da equipe do gerente: ")

    gerente = Gerente(identificador, nome, idade, salario, departamento, tamanho_equipe)
    registrarFuncionario(gerente)

def registrarFuncionario(funcionario):
    if verificarExistenciaFuncionario(funcionario.identificador):
        print("\n--- Já existe um funcionário registrado com o identificador indicado! ---")
        return

    funcionarios.append(funcionario)
    print("\n--- Funcionário cadastrado com sucesso! ---")

def verificarExistenciaFuncionario(identificador):
    funcionario = procurarFuncionario(identificador)

    return funcionario is not None


def procurarFuncionario(identificador):
    for funcionario in funcionarios:
        if funcionario.identificador == identificador:
            return funcionario

    return None

#def listarFuncionarios():

#def consultarFuncionarioPorCodigo():

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
    print("\n--- Insira uma opção válida! ---")

while True:
    exibirMenuPrincipal()
    opcao = input("\nInsira a opção desejada: ")
    if executarOpcao(opcao):
        break