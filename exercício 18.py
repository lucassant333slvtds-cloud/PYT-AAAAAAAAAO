import math
An = float(input("Digite um angulo qualquer: "))
sen = math.sin(math.radians(An))
cos = math.cos(math.radians(An))
tan = math.tan(math.radians(An))
print ("O angulo de {} tem o seno de {:.2f}, cosseno é {:.2f} e a tangente é {:.2f} ".format(An,sen,cos,tan))
