import pygame
from time import sleep

A = float(input("Digite a primeira medida: "))
B = float(input("Digite a segunda medida: "))
C = float(input("Digite a terceira medida: "))

print("Processando...")
sleep(2)

if A + B > C and A + C > B and B + C > A:
    print("Dá pra fazer um triângulo massa ein!!!(⓿_⓿)😎")
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
