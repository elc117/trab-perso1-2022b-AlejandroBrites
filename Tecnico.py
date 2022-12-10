from Pessoa import Pessoa

class Tecnico(Pessoa):

    def __init__(self, nome, time, salario):
        super().__init__(nome, time)
        self.__salario = salario
        print("Técnico Criado")

    def get_salario (self):
        return self.__salario

    def set_salario (self, salario):
        self.__salario = salario

    def calcularSalarioAnual (self):
        return self.__salario*12

    def apresentacao(self):
        print(self._nome, "é o técnico do time", self._time)