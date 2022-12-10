class Pessoa:

    def __init__(self, nome, time):
        self._nome = nome
        self._time = time
        print("Pessoa Criada")

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


class Tecnico(Pessoa):

    def __init__(self, nome, time, salario):
        super().__init__(nome, time)
        self._salario = salario
        print("Técnico Criado")

    def get_salario (self):
        return self._salario

    def set_salario (self, salario):
        self._salario = salario

    def calcularSalrioAnual (self):
        return self._salario*12

    def apresentacao(self):
        print(self._nome, "é o técnico do time", self._time)


class Jogador(Pessoa):

    def __init__(self, nome, time, apelido, posicao, camisa, salario):
        super().__init__(nome, time)
        self._apelido = apelido
        self._posicao = posicao
        self._camisa = camisa
        self._salario = salario
        print("Jogador Criado")

    def get_apelido (self):
        return self._apelido

    def set_apelido (self, apelido):
        self._apelido = apelido
    
    def get_posicao (self):
        return self._posicao

    def set_posicao (self, posicao):
        self._posicao = posicao

    def get_camisa (self):
        return self._camisa

    def set_camisa (self, camisa):
        self._camisa = camisa
    
    def get_salario (self):
        return self._salario

    def calcularSalrioAnual (self):
        return self._salario*12.00

    def apresentacao(self):
        print(self._nome, "é o jogador camisa", self._camisa, "do time", self._time)

class Torcedor(Pessoa):

    def __init__(self, nome, time):
        super().__init__(nome, time)
        print("Torcedor Criado")

    def apresentacao(self):
        print(self._nome, "é um torcedor do time", self._time);


p1 =  Pessoa('Luiz', 'A')
p1.apresentacao()
p2 =  Jogador('Luiz', 'A', 'Lu', 'lateral', 10, 1000)
p2.apresentacao()
p3 =  Tecnico('Luiz', 'A', 10000)
p3.apresentacao()
p4 =  Torcedor('Luiz', 'A')
p4.apresentacao()