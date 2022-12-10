from Pessoa import Pessoa

class Jogador(Pessoa):

    def __init__(self, nome, time, posicao, camisa, salario):
        super().__init__(nome, time)
        self.__posicao = posicao
        self.__camisa = camisa
        self.__salario = salario
        print("Jogador Criado")

    def get_posicao (self):
        return self.__posicao

    def set_posicao (self, posicao):
        self.__posicao = posicao

    def get_camisa (self):
        return self.__camisa

    def set_camisa (self, camisa):
        self.__camisa = camisa

    def get_salario (self):
        return self.__salario

    def set_salario (self, salario):
        self.__salario = salario

    def calcularSalarioAnual (self):
        return self.__salario*12.00

    def apresentacao(self):
        print(self._nome, "é o jogador camisa", self.__camisa, "do time", self._time)