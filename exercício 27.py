nome = str(input("Digite seu nome: ")).strip()
D = nome.split()
print("O seu primeiro nome é {}".format(D[0]))
print("O seu ultimo nome é {}".format(D[len(D)-1]))
