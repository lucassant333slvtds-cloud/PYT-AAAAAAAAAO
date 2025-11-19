print("\033[1;32m=\033[m"*40)
print("\033[1;33m TERMOS DE UMA PA\033[m")
print("\033[1;32m=\033[m"*40)
primeiro_termo = int(input("Digite o primeiro termo: "))
Razão = int(input("Digite a razão: "))

decimo = primeiro_termo + (10-1) * Razão
for c in range(primeiro_termo,decimo,Razão):
    print(c, end=" ➡  ")
print("CABO!")
