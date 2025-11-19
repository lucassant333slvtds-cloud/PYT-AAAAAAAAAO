print("\033[7;39;40m==========\033[m\033[7;39;40m==========\033[m\033[7;39;40m==========\033[m")
print("\033[7;39;40m===\033[m\033[1;32;40m=======Lojas Cjay=======\033[m\033[7;39;40m===\033[m")
print("\033[7;39;40m==========\033[m\033[7;39;40m==========\033[m\033[7;39;40m==========\033[m")

    


Valor_compra = float(input("\033[1;34mValor da compra: \033[mR$"))

print("\033[1;33m="*9,"###","=========\033[m","\033[1;33m="*9,"###")


print("\033[1;33mFORMA DE PAGAMENTO                ||\033[m")


print("\033[1;35m[ 1 ]\033[m \033[1;36mÀ vista dinheiro/cheque\033[m     \033[1;33m||\033[m")
print("\033[1;35m[ 2 ]\033[m \033[1;36mÀ vista cartão\033[m              \033[1;33m||\033[m")
print("\033[1;35m[ 3 ]\033[m \033[1;36m2x no cartão\033[m                \033[1;33m||\033[m")
print("\033[1;35m[ 4 ]\033[m \033[1;36m3x ou mais no cartão\033[m        \033[1;33m||\033[m")



print("\033[1;34mQual sua opção? \033[m                  \033[1;33m||\033[m")

Opção = float(input(""))

print("\033[1;33m="*9,"###","=========\033[m","\033[1;33m="*9,"###")


valor_totalOP1 = Valor_compra - (Valor_compra * 10 / 100)
valor_totalOP2 = Valor_compra - (Valor_compra * 5 / 100)
valor_totalOP3 = Valor_compra 
valor_totalOP4 = Valor_compra + (Valor_compra * 20 / 100)



if Opção == 1:
    print("\033[1;36mO valor de sua compra será de\033[m \033[1;32mR${}\033[m \033[1;36mcom 10 % de desconto aplicado!!".format(valor_totalOP1))

elif Opção == 2:
    print("\033[1;36mO valor de sua compra será de\033[m \033[1;32mR${}\033[m \033[1;36mcom 5 % de desconto aplicado!!".format(valor_totalOP2))

elif Opção == 3:
    print("\033[1;36mO valor de sua compra será de\033[m \033[1;32mR${}\033[m \033[1;36msem juros!!".format(valor_totalOP3))

else:
    
    Parcelas = float(input("\033[1;34mQuantas Parcelas? "))
    valor_parcela = valor_totalOP4 / Parcelas
    print("\033[1;36mO valor de sua compra será parceladas em\033[m \033[1;31m{:.0f}X\033[m \033[1;36me ficará no valor de\033[m \033[1;32mR${:.2F}\033[m \033[1;36mcom\033[1;31m 20%\033[m \033[1;36mde juros aplicados!!\033[m".format(Parcelas,valor_totalOP4))
