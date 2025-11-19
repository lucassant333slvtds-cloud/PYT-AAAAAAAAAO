DA = int(input("Quantos dias alugados? "))
KmR = float(input("Quantos quilometros rodados? Km"))
Dia = 60.00 * DA
Kms = 0.15 * KmR
TOTAL = Dia + Kms
print ("O total a pagar será de R${:.2f}".format(TOTAL))
