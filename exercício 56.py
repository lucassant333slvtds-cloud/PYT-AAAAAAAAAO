soma_idade = 0 
média_idade = 0 
maior_idade_homem = 0
nome_mais_vei = ""
Tot_muie_M20 = 0
for P in range(1,5):
    print(f"\033[1;33m=-=-=-=-={P}° Pessoa=-=-=-=-=")
    N = str(input("\033[1;32mNome: ")).strip()
    I = int(input("Idade: "))
    S = str(input("Sexo [M/F]:")).strip()
    print(f"\033[1;33m=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    soma_idade += I
    média_idade = soma_idade / 4
    if P == 1 and S in "Mm":
        maior_idade_homem += I
        nome_mais_vei = N
    if S in "Mm" and I > maior_idade_homem:
        maior_idade_homem += I
        nome_mais_vei = N
    if S in "Ff" and I <= 20:
        Tot_muie_M20 += 1
print(f"A média da idade do grupo é de {média_idade:.0f} anos.\n"
      f"O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_vei}\n"
      f"Ao todo são {Tot_muie_M20} mulheres com menos de 20 anos.")
