Peso = float(input("\033[1;34mQual o seu peso atual?\033[m "))
Altura = float(input("\033[1;34mQual sua altura atualmente?\033[m "))
imc = Peso / (Altura ** 2)
print("O \033[1;32mIMC\033[m desta pessoa é de {:.1F}".format(imc))
if imc <= 18.5:
    print("Parabens, você está na faixa ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print(F"Parabens, você está na faixa de PESO IDEAL")
elif 25 <= imc < 30:
    print(F"Parabens, você está na faixa de SOBRE PESO")
elif 30 <= imc < 40:
    print(F"Parabens, você está na faixa de OBESIDADE")
else: 
    print(F"Parabens, você está na faixa de OBESIDADE MÓRBIDA")
