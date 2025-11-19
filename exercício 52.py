print("                              \033[1;33m##=-=-=-=-=-++=-=-=-=-++=-=-=-=-++-=-=-=-=-=-##\033[m")
print("                              \033[1;33m||\033[m       \033[1;35mVERIFICADOR DE NÚMEROS PRIMOS\033[m       \033[1;33m||\033[m")
print("                              \033[1;33m##=-=-=-=-=-++=-=-=-=-++=-=-=-=-++-=-=-=-=-=-##\033[m")
tot = 0
Num = int(input("                              \033[1;35mDigite um número:\033[m "))
for c in range(1,Num+1):
    if Num % c == 0:
        print("\033[1;36m",end="")
        tot += 1
    else:
        print("\033[1;31m",end="")
    print(f"{c}", end=", ")
print(f"\033[m\nO numero {Num} foi divisivel por {tot} veses.")
if tot == 2:
    print("Então por este motivo ele é primo")
else:
    print("Então por este motivo ele não é primo")
