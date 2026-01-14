A = float(input("Digite o primeiro número: "))
B = float(input("Digite o segundo número: "))
C = float(input("Digite o terceiro número: "))
#Calculo do menor número!!!!!!!!
menor = A
if B<A and B<C:
    menor = B
if C<A and C<B:
    menor = C
#__________________________________________________________________________________
#Calculo do número mediano!!!
mediano = A
if B > A and B < C:
    mediano = B
if C > A and C < B:
    mediano = C
#__________________________________________________________________________________
#Calculo do maior número!!!!!!!!!!!!!!!!
maior = A
if B > A and B > C:
    maior = B
if C > A and C > B:
    maior = C
#___________________________________________________________________________________
#CABO!!

print("O menor número é{}\nO número mediano é {}\nE o maior número é {}".format(menor,mediano,maior))
