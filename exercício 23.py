N = int((input("Digite um valor: ")))
U = N // 1 % 10
D = N //10 % 10
C = N // 100 % 10
M = N // 1000 % 10
#U = (N[3:4])
#D = (N[2:3])
#C = (N[1:2])
#M = (N[0:1])
print("O numero {} tem:\n{} unidades\n{} dezenas\n{} centenas\n{} milhar".format(N,U,D,C,M))

