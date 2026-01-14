nome = str(input("Digite seu nome: ")).lower().strip()
print("A letra A aparece {} vezes na frase".format(nome.count("a")))
print("A letra A apareceu primeiro na  {}° posição".format(nome.find("a")+1))
print("A letra A apareceu por ultimo na {}° posição".format(nome.rfind("a")+1))
