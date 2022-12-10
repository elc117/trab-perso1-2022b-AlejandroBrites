class Pessoa:

    def __init__(self, nome, time):
        self._nome = nome
        self._time = time

    def apresentacao(self):
        print(self._nome + " é uma pessoa que gosta do time " + self._time ".")


class Técnico(Pessoa):

    def __init__(self, nome, time, salario):
        super().__init__(nome, time)
        self.__salario = salario
        print("Técnico Criado")

    def apresentacao(self):
        print(self._nome + " é o técnico do time " + self._time ".")


class Jogador(Pessoa):

    def __init__(self, nome, time, apelido, posicao, camisa, salario):
        super().__init__(nome, time)
        self.__apelido = apelido
        self.__posicao = posicao
        self.__camisa = camisa
        self.__salario = salario
        print("Jogador Criado")

    def apresentacao(self):
        print(self._nome + " é o jogador camisa" + self.__camisa + " do time " + self._time ".")

class Torcedor(Pessoa):

    def __init__(self, nome, time):
        super().__init__(nome, time)
        print("Torcedor Criado")

    def apresentacao(self):
        print(self._nome + " é um torcedor do time " + self._time ".");
