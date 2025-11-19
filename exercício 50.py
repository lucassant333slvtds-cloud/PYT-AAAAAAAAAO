soma = 0
count = 0
for inp in range(1,7):
    N = int(input(f"Digite o {inp}° valor: "))
    if N % 2 == 0:
        soma += N
        count += 1
if count == 1:
        print(f"Voce informou {count} número par portanto o resultado da soma é {soma}")
else:
     print(f"Voce informou {count} numeros pares e o resultado da soma deles é {soma}")
