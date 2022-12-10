class Pessoa:

    def __init__(self, nome, time):
        self._nome = nome
        self._time = time

    def get_nome (self):
        return self._nome

    def set_nome (self, nome):
        self._nome = nome

    def get_time (self):
        return self._time

    def set_time (self, time):
        self._time = time

    def apresentacao(self):
        print(self._nome, "é uma pessoa que gosta do time", self._time)