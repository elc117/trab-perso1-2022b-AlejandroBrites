from Pessoa import Pessoa

class Jogador(Pessoa):

    def __init__(self, nome, time, apelido, posicao, camisa, salario):
        super().__init__(nome, time)
        self.__apelido = apelido
        self.__posicao = posicao
        self.__camisa = camisa
        self.__salario = salario
        print("Jogador Criado")

    def get_apelido (self):
        return self.__apelido

    def set_apelido (self, apelido):
        self.__apelido = apelido
    
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

    def calcularSalarioAnual (self):
        return self.__salario*12.00

    def apresentacao(self):
        print(self._nome, "é o jogador camisa", self.__camisa, "do time", self._time)