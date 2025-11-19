PrimeiroN = float(input("Digite o primeiro valor: "))
SegundoN = float(input("Digite o segundo valor: "))
if PrimeiroN > SegundoN or SegundoN < PrimeiroN:
    print(f"O Primeiro valor é maior")
elif PrimeiroN < SegundoN or SegundoN > PrimeiroN:
    print(f"O Segundo valor é maior que o Primeiro")
elif PrimeiroN == SegundoN or SegundoN == PrimeiroN:
    print ("Os Dois valores são iguais")
