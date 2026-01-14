from datetime import date
Ano = int(input("Digite o ano em que voce nasceu: "))
AnoAT = date.today().year
idade = AnoAT - Ano
AnosR = idade - 18
AnodeAlistamento = (Ano + 18)

if idade < 18:
    print(f"Você nasceu em {Ano} tem {idade} em {AnoAT}.\nAinda faltam {AnosR} para o alistamento.\nSeu alistamento será em {AnodeAlistamento}")
elif idade > 18:
    print(f"Você nasceu em {Ano} tem {idade} em {AnoAT}.\nVoce ja deveria ter se alistado à {AnosR} anos.\nSeu alistamento foi em{AnodeAlistamento}")
elif idade == 18:
    print(f"Você nasceu em {Ano} tem {idade} em {AnoAT}.\nVocê deve se alistar imediatamente pois seu ano de alistamento é {AnodeAlistamento}")
else:
    print("Isso ai n da certo n ein!!!!!")
    