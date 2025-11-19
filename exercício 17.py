from math import sqrt
CO = float(input("Comprimento do cateto oposto"))
CA = float(input("Comprimento do cateto adjacente"))
H = (CO ** 2 + CA ** 2) ** (1/2)
print ("O valor da hipotenusa é {}".format(H))
