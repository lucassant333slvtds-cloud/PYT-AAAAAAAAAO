nome = str(input('\033[1;35mQual o nome do aluno? \033[m'))
n1 = float(input('\033[1;34mPrimeira nota do aluno: \033[m'))
n2 = float(input('\033[1;33mSegunda nota do aluno: \033[m'))
M = (n1 + n2) / 2
print ("A média das notas do aluno \033[4;32m{}\033[m entre \033[1;32m{:.1f}\033[m e \033[1;32m{:.1f}\033[m é igual a \033[1;30;47m{:.1f}\033[m".format(nome,n1,n2,M))
