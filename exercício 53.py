print("                              \033[1;33m##=-=-=-=-=-++=-=-=-=-++=-=-=-=-++-=-=-=-=-=-##\033[m")
print("                              \033[1;33m||\033[m       \033[1;35mDETECTOR DE PALINDROMO\033[m              \033[1;33m||\033[m")
print("                              \033[1;33m##=-=-=-=-=-++=-=-=-=-++=-=-=-=-++-=-=-=-=-=-##\033[m")



#Tem jeito de usar o for mas eu n entendi saporra
#palavra = str(input("Digite a palavra para fazer a análize: "))
#invertida = ""
#for letra in palavra:
#    invertida = letra + invertida
#print(invertida)

palavra = str(input("Digite sua palavra: "))
invertida = palavra[::-1]
if invertida == palavra:
    print("\033[1;32mParabeeens você encontrou um PALINDROMO!!")
else:
    print("\033[1;31mIsso não é um PALINDROMO!")

