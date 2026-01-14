nome = str(input("Qual o nome do colaborador? "))
S = float(input("Qual o salário dele? R$"))
PA = float(input("Qual a porcentagem do aumento do colaborador? %"))
Pd = float(input("Qual a porcentagem do desconto do colaborador? %"))
PDA = PA / 100
PDD = Pd / 100
Cpda = S * PDA
Cpdd = S * PDD
VCPDA = S + Cpda
VCPDD = S - Cpdd
print ("O colaborador {} tem o sálario Bruto de R${:.2F} e se ele receber um aumento de %{:.0F} \no salário líquido dele será de R${:.2F} \n(✿◕‿◕✿) \n Mas caso o colaborador {} não receber nenhum aumento e sim um desconto de %{:.0f} ele \nirá receber um total de R${:.2f} de salário líquido.\n┗|｀O′|┛ ".format(nome,S,PA,VCPDA,nome,Pd,VCPDD))
