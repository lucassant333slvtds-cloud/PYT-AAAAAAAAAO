import math
import pygame
from time import sleep

A = float(input("Digite a primeira medida: "))
B = float(input("Digite a segunda medida: "))
C = float(input("Digite a terceira medida: "))

if A + B > C and A + C > B and B + C > A:
    print("Dá pra fazer um triângulo massa ein!!!(⓿_⓿)😎")
    if A == B == C:
        print("Este triangulo é \033[1;36mEquilátero\033[m")
    if A == B or B == C or A == C:
        if not A == B == C:
            print("Este triangulo é \033[1;36mIsósceles\033[m")
    if A != B and B != C and A != C:
        print("Este triangulo é \033[1;36mEscaleno\033[m")
else:
    print("Processando.")
    sleep(1)
    print("Processando..")
    sleep(1)
    print("Processando...")
    sleep(1)
    print("Processando.")
    sleep(1)
    print("Processando..")
    sleep(1)
    print("Processando...")
    sleep(1)
    print("Processando.")
    sleep(1)
    print("Processando..")
    sleep(1)
    print("Processando...")
    sleep(1)
    print("Processando.")
    sleep(1)
    print("Processando..")
    sleep(1)
    print("Processando...")
    sleep(1)


    pygame.init()
    pygame.mixer.music.load("failed-295059.mp3")  # coloque esse arquivo na mesma pasta do script
    pygame.mixer.music.play()

    # Espera o som terminar de tocar
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(0)

    print("Achou que eu tinha bugado neh kkkkkkkkk😎\nEsse numeru aí não dá pra virar triângulo não (〜￣▽￣)〜")
