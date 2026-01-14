from time import sleep
N1 = int(input("\033[1;34mPrimeiro valor: \033[m"))
N2 = int(input("\033[1;34mSegundo valor: \033[m"))
sleep(0.5)
opcao = 0
while True:
    print('''\033[1;33m    (1)Somar
    (2)Subtrair
    (3)Multiplicar
    (4)Dividir
    (5)Maior número entre os valores
    (6)Novos valores
    (7)Sair\033[m''')
    sleep(1)
    opcao = int(input("\033[1;33m>>>>\033[m\033[1;34mQual a sua opção?\033[m\033[1;33m<<<<\033[m\n            "))
    if opcao == 1:
        R1 = N1 + N2
        print(f"\033[1;34mA soma entre {N1} e {N2} é igual à\033[m \033[1;32m{R1}\033[m")
        sleep(2)
        print("\033[1;34mAgora pode escolher uma nova opção!\033[m" )
        sleep(2)
    elif opcao == 2:
        R2 = N1 - N2
        print(f"O valor {N1} subtraido pelo valor {N2} é igual à {R2}")
        sleep(2)
        print("\033[1;34mAgora pode escolher uma nova opção!\033[m" )
        sleep(2)
    elif opcao == 3:
        R3 = N1 * N2
        print(f"O número {N1} multiplicado  pelo número {N2} é igual à {R3}")
        sleep(2)
        print("\033[1;34mAgora pode escolher uma nova opção!\033[m" )
        sleep(2)
    elif opcao == 4:
        R4 = N1 / N2
        print("")
    elif opcao == 5:
        if N1 > N2:
            print(N1)
        else:
            print(N2)
    elif opcao == 6:
        print("Informe os valores novamente!")
        N1 = int(input("Primeiro valor: "))
        N2 = int(input("Segundo valor: "))
        print("Finalizando.")
    elif opcao == 7:
        sleep(0.5)
        print("Finalizando..")
        sleep(0.5)
        print("Finalizando...")
        sleep(0.5)
        print("Finalizando.")
        sleep(0.5)
        print("Finalizando..")
        sleep(0.5)
        print("Finalizando...")
        sleep(0.5)
        print("Finalizando.")
        sleep(0.5)
        print("Finalizando..")
        sleep(0.5)
        print("Finalizando...")
        sleep(0.5)
        print(">>>>Pronto!<<<<")

        print("FALOU ENTAO, VOLTE SEMRPRE!")
        break
