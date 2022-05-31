import Funcionario
import Cliente

c1 = Cliente("Joaquim", "20/05/1990", "Fernando", "Juliana", 1000, 2)
c2 = Cliente("Francisco", "15/09/1995", "Antônio", "Francisca", 200, 1)

f1 = Funcionario("Andreson", "14/04/1999", "Cicero", "Diana", 1600, "Auxiliar de produção")
f2 = Funcionario("Alice", "16/06/1997", "Mauricio", "Jaqueline", 2300, "Gerente de produção")

print("Nome do cliente: {}".format(c1._nome))
print("Débitos: {}".format(c1.debitos))
print("-------------")
print("Nome do cliente: {}".format(c2.nome))
print("Débitos: {}".format(c2.debitos))
print("-------------")
print("Setor do funcionario {}".format(f1.nome))
print(f1.setor)
print("-------------")
print("Cargo Funcionario {}".format(f2.nome))
print(f2.setor)
