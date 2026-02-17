#nome = str(input("Qual é o seu nome? "))
#print("Seja bem vindo {:20}".format(nome))
#print('Se bem vindo {:>20}'.format(nome))
#print("Seja bem vindo {:<20}".format(nome))
#print("Seja bem vindo {:^20}".format(nome))
#print("Seja bem vindo {:=^20}".format(nome))
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {},o produto é {} é a divisão {:.3f}".format(s, m, d),end=" ")
print("A divisão inteira {} e potencia {}".format(di, e))