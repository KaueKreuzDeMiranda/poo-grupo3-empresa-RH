# Sistema de RH — POO Grupo 3

Aplicação de console em Python para gerenciamento de funcionários de uma empresa, desenvolvida para praticar Programação Orientada a Objetos.

## Funcionalidades

- Cadastro de **Estagiário**, **Desenvolvedor** e **Gerente**
- Listagem de todos os funcionários
- Consulta de funcionário por identificador
- Execução de método polimórfico (`trabalhar()`) para todos os funcionários
- Execução de métodos exclusivos de cada cargo
- Validação de dados de entrada e regras de negócio

## Conceitos de POO aplicados

| **Herança** |
| **Encapsulamento** |
| **Polimorfismo** |

## Regras de validação

- Idade mínima: **14 anos**
- Salário: deve ser **maior que zero**
- Tamanho da equipe (Gerente): **não pode ser negativo**
- Identificador: **único** por funcionário
- Entradas numéricas inválidas são solicitadas novamente

## Estrutura do projeto

```
.
├── <main>.py
└── model/
    ├── Funcionario.py
    ├── Estagiario.py
    ├── Desenvolvedor.py
    └── Gerente.py
```

## Requisitos

- Python 3.6+
- Nenhuma dependência externa

## Menu

```
1 - Cadastrar Estagiário
2 - Cadastrar Desenvolvedor
3 - Cadastrar Gerente
4 - Listar funcionários
5 - Consultar funcionário por identificador
6 - Realizar função polimórfica
7 - Executar métodos exclusivos
0 - Encerrar sistema
```
