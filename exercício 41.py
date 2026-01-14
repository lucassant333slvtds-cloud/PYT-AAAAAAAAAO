from datetime import date
ano = int(input("Ano de nacimento: "))
anoAT = date.today().year
idade = anoAT - ano
print(f"O atleta tem {idade}")
if idade <= 9:
    print("Classificação: Mirim")
elif 9 <= idade < 14:
    print("Classificação: Infantil")
elif 14 <= idade < 19:
    print(f"Classificação: Junior")
elif 19 <= idade < 25:
    print(f"Classificação: Sênior")
elif idade >= 25:
    print(f"Classificação: Master")
