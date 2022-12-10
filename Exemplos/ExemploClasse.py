class Jogador:

    def __init__(self, nome, time, apelido, posicao, camisa, salario):
        self.__nome = nome
        self.__time = time
        self.__apelido = apelido
        self.__posicao = posicao
        self.__camisa = camisa
        self.__salario = salario
        print("Jogador Criado")

    def calcularSalrioAnual (self):
        return self.__salario*12
