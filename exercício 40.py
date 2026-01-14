nome = str(input("Digite o nome do aluno: "))
N1 = float(input("Digite a primeira nota do aluno: "))
N2 = float(input("Digite a segunda nota do aluno: "))

mediaA = (N1 + N2) / 2

print("A primeira nota do aluno {} foi {} e a segunda nota foi {} então sua média foi {:2}".format(nome,N1,N2,mediaA))

if mediaA >= 7.0:
    print(f"Parabens {nome} você foi      \033[1;32mA    P    R    O    V    A    D    O\033[m")
elif mediaA < 5.0:
    print(f"Infelismente o aluno {nome} foi      \033[1;31mR    E    P    R    O    V    A    D    O\033[m")
elif 5.0 <= mediaA < 7.0:
    print(f"Infelismente o aluno {nome} está de      \033[1;33mR    E    C   U    P    E    R    A    Ç    Ã    O\033[m")
