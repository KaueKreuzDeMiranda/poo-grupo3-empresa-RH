class Funcionario:
    def __init__(self, identificador, nome, idade, salario):
        self.__identificador = identificador
        self.__nome = nome
        self.__idade = idade
        self.__salario = salario

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if idade < 14:
            raise ValueError("A idade mínima para trabalhar é 14 anos.")
        self.__idade = idade

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    def __str__(self):
        return (f"\nID: {self.identificador}"
                f"\nNome: {self.nome}" 
                f"\nIdade: {self.idade}"
                f"\nSalario: {self.salario}")

    def trabalhar(self):
        return f"\n{self.nome} está realizando suas atividades na empresa."