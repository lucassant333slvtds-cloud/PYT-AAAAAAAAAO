N = int(input("\033[1;36mDigite um número: \033[m"))
print('Escolha uma das 3 opções de conversores')
Opção = str(input("( 1 ) Conversor para BINÁRIO. \n( 2 ) Conversor para  OCTAL.\n( 3 ) Conversor para HEXADECIMAL.\nDigite a opção aqui: " ))


if Opção == "1":
    print(f"O número {N} em BINÁRIO é \033[1;32m{bin(N)[2:]}\033[m")#[2:] Tira 2 primeiro digito do nomero que são só pra mostar que aquele resultado é binário.
elif Opção == "2":
    print(f"O número {N} em OCTAL é \033[1;32m{oct (N)[2:]}\033[m")
elif Opção == "3":
    print(f"O número {N} em HEXADECIMAL é \033[1;32m{hex(N)[2:].upper()}\033[m")#.upper deixa tudo em maiusculo
else:
    print("ISSO AI N DA CERTO N IRMÃO!!!")
