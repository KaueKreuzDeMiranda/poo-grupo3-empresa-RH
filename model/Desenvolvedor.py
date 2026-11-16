from Funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, identificador, nome, idade, salario, nivel, stack):
        super().__init__(identificador, nome, idade, salario)
        self.__nivel = nivel
        self.__stack = stack

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    @property
    def stack(self):
        return self.__stack

    @stack.setter
    def stack(self, stack):
        self.__stack = stack

    def __str__(self):
        return (f"{super().__str__()}"
                f"\nNível: {self.__nivel}"
                f"\nStack: {self.__stack}")