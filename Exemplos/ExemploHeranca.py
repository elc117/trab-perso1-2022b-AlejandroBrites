class Pessoa:

    def __init__(self, nome, time):
        self._nome = nome
        self._time = time


class Técnico(Pessoa):

    def __init__(self, nome, time, salario):
        super().__init__(nome, time)
        self.__salario = salario
        print("Técnico Criado")


class Jogador(Pessoa):

    def __init__(self, nome, time, apelido, posicao, camisa, salario):
        super().__init__(nome, time)
        self.__apelido = apelido
        self.__posicao = posicao
        self.__camisa = camisa
        self.__salario = salario
        print("Jogador Criado")

class Torcedor(Pessoa):

    def __init__(self, nome, time):
        super().__init__(nome, time)
        print("Torcedor Criado")
