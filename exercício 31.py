distancia = float(input("Qual a distância da viagem em km? "))
valor_km = float(input("Qual o valor em reais de cada km? "))
desconto = input("Tem desconto? (sim/não): ").strip().lower()

valor_total = distancia * valor_km

if desconto == "sim":
    valor_desconto = float(input("Qual o valor deste desconto em reais? ")) 

print("\nVocê está prestes a começar uma viagem de {} km.".format(distancia))
print("O preço da sua viagem será de R${:.2f} reais.".format(valor_total))
print("TENHA UMA BOA VIAGEM (✿ ◠ ‿ ◠ )")
