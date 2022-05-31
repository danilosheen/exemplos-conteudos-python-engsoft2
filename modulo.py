from Funcionario import Funcionario
from Cliente import Cliente
from Pessoa import Pessoa

c1 = Cliente("Joaquim", "20/05/1990", "Fernando", "Juliana", 1000, 2)
c2 = Cliente("Francisco", "15/09/1995", "Antônio", "Francisca", 200, 1)

f1 = Funcionario("Anderson", "14/04/1999", "Cicero", "Diana", 1600, "Auxiliar de producao")
f2 = Funcionario("Alice", "16/06/1997", "Mauricio", "Jaqueline", 2300, "Gerente de producao")

print("Nome do(a) cliente: {}".format(c1.getNome()))
print("Debitos: {}".format(c1.getDebito()))
print("-------------")
print("Nome do(a) cliente: {}".format(c2.getNome()))
print("Debitos: {}".format(c2.getDebito()))
print("-------------")
print("Setor do funcionario(a): {}".format(f1.getNome()))
print(f1.getSetor())
print("-------------")
print("Setor Funcionario(a): {}".format(f2.getNome()))
print(f2.getSetor())
