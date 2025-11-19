Velocidade = float(input("Qual a velocidade do carro? "))
print("-=-" * 41)
multa = float(Velocidade - 80.) * 7
if Velocidade <= 80.0:
    print("Tenha um bom dia (●'◡'●) e continue dirigindo com segurança! ")
elif Velocidade > 80.0:
    print("\033[31mMULTADO!!! \033[37mVocê excedeu a velocidade máxima de 60 km e deverá pagar uma multa de \033[32m R${} reais.\n\033[90mSE FUDEU ( ͡ಠ ʖ̯ ͡ಠ)\033[0m".format(multa))
