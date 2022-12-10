from Pessoa import Pessoa

class Torcedor(Pessoa):

    def __init__(self, nome, time):
        super().__init__(nome, time)
        print("Torcedor Criado")

    def apresentacao(self):
        print(self._nome, "é um torcedor do time", self._time);