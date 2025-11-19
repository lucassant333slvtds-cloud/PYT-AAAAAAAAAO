from random import randint
from time import sleep
print("-=" * 50)
print("Vou pensar em um número entre 0 e 5\nTente adivinhar se tu é bom mermo")

computador = randint(0,5)
jogador = int(input("Qual numero eu pensei ?"))
print("processando...")
sleep(3)
if jogador == computador: 
    print("BOA!!! Vc Cagou muito mas ta bão")
    print("))))|||(((\n(   👀   )\n(   👄   )\n\///✌🏿\///👍🏿\n|        |\n|        |\n|===@-===|")
else:
    print("ERROOOOOOOOOOU!!!!! Perdeu pq tu é muito ruim. Vai pro tigrinho que lá é mais facil\nOTAAAAAAAATIOOO!!!!!")
    print("          ))))|||(((\n          ( 👁     👁 )\n          (    👅   )\n        👎🏿\\/👎🏿\\/ \n          |        |\n          |        |\n          |===@-===|")
print("O número que eu pensei foi o {} (〜￣▽￣)〜".format(computador))
