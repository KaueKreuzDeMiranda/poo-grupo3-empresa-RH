from model.Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, identificador, nome, idade, salario, departamento, tamanho_equipe):
        super().__init__(identificador, nome, idade, salario)
        self.__departamento = departamento
        self.__tamanho_equipe = tamanho_equipe

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    @property
    def tamanho_equipe(self):
        return self.__tamanho_equipe

    @tamanho_equipe.setter
    def tamanho_equipe(self, tamanho_equipe):
        if tamanho_equipe < 0:
            raise ValueError("\n--- O tamanho da equipe não pode ser negativo. ---")
        self.__tamanho_equipe = tamanho_equipe

    def __str__(self):
        return (f"{super().__str__()}"
                f"\nDepartamento: {self.__departamento}"
                f"\nTamanho da equipe: {self.__tamanho_equipe}")

    def trabalhar(self):
        return f"{self.nome} está gerenciando o departamento de {self.__departamento} e liderando uma equipe de {self.__tamanho_equipe} pessoas."