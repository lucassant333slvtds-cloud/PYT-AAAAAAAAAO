Salário = float(input("Qual o salário do funcionário? "))
if Salário <= 1518.0:
    aumento = Salário * 15 / 100
    Nsalario = Salário + aumento
    print("O Funcionário que ganhava R${} terá um aumento de R${} totalizando um salário de R${}".format(Salário,aumento,Nsalario))
else:
    aumento = Salário * 10 / 100
    Nsalario = Salário + aumento
    print("O Funcionário que ganhava {}, terá um aumento de R${} totalizando um salário de R${}".format(Salário,aumento,Nsalario))
