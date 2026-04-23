nome = str(input("Qual o seu nome? "))

if nome == "Gustavo":
    print("Que nome bonito")
    print("Olá {}".format(nome))
elif nome == "Paulo" or nome == "Maria" or nome == "João":
    print("Que nome popular")
elif nome in "Ana jose karyta juliana":
    print("nome feminino!")

else:
    print("Nome normal")
    print("Olá {}".format(nome))