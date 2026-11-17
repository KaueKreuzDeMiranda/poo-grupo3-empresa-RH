from model.Funcionario import Funcionario

class Estagiario(Funcionario):
    def __init__(self, identificador, nome, idade, salario, curso, tutor):
        super().__init__(identificador, nome, idade, salario)
        self.__curso = curso
        self.__tutor = tutor

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def tutor(self):
        return self.__tutor

    @tutor.setter
    def tutor(self, tutor):
        self.__tutor = tutor

    def __str__(self):
        return (f"{super().__str__()}"
                f"\nCurso: {self.__curso}"
                f"\nTutor: {self.__tutor}")

    def trabalhar(self):
        return f"\n{self.nome} está estagiando na área de {self.__curso}, auxiliando nas tarefas sob supervisão de {self.__tutor}."