pesos = []
for c in range(1,6):
    peso = float(input(f"Qual o peso da {c}° pessoa? "))
    pesos.append(peso)
print(f"O maior peso lido é o de {max(pesos)}\nO menor peso lido é o de {min(pesos)}")


