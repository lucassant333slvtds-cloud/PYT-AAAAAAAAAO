from random import randint
from time import sleep

print("+-----"*6)
print("Vamo jogar um jogo em parcero!!")
sleep(1)
print("Baguio é o seguinte,\nVou pensa num numero ae de 1 à 10")
sleep(1)

IA = randint(1, 10)
acertou = False

while not acertou:
    jogador = int(input("Qual o número que eu pensei? "))
    print("processando...")
    sleep(0.5)

    if jogador == IA:
        acertou = True
        print("""
))))|||(((
(   👀   )
(   👄   )
\\///✌🏿\\///👍🏿
|        |
|        |
|===@-===|
BOAAAAAA
""")
    else:
        print("""
         ))))|||(((
          ( 👁     👁 )
          (    👅   )
        👎🏿\\/👎🏿\\/
          |        |
          |        |
          |===@-===|
ERROOOOOOOOOOU!!!!! Perdeu pq tu é muito ruim.
Mas tenta de novo ae!
""")
