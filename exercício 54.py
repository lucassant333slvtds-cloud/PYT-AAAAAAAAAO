contMenor = 0
contMaior = 0
for c in range(1,8):
    ano = int(input(f"Qual o ano em que a {c}° pessoa nasceu? "))
    if ano <= 2007:
        contMaior += 1
    else:
        contMenor += 1 
print(f"Ao todo tivemos {contMenor} pessoas menores de idade e {contMaior} pessoas que são maiores de idade.")
