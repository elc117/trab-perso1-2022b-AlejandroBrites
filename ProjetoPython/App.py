from Pessoa import Pessoa
from Jogador import Jogador
from Tecnico import Tecnico
from Torcedor import Torcedor

p1 =  Pessoa('Roberto', 'Barcelona')
j1 =  Jogador('Neymar', 'Brasil', 'atacante', 10, 23000000)
T1 =  Torcedor('Bruno', 'Internacional')
t1 =  Tecnico('Tite', 'Brasil', 1600000)

p1.apresentacao()
j1.apresentacao()
T1.apresentacao()
t1.apresentacao()

print("O salário de ", j1.get_nome(), " é cerca de ", j1.calcularSalarioAnual(), " por ano")
print("O salário de ", t1.get_nome(), " é cerca de ", t1.calcularSalarioAnual(), " por ano")






