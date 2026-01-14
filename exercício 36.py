from time import sleep

# Título
print("\033[1;36;42m-=-\033[m"*23)
print("\033[42m = \033[m\033[32m🤑 Calculador de emprestimos 💲💲💲\033[m                            \033[42m = \033[m")
print("\033[42m = \033[m\033[1;33mVamo calcular esse emprestimo e ve se da pra aprovar saporra ae\033[m\033[42m = \033[m")
print("\033[1;36;42m-=-\033[m"*23)
sleep(1)

# Questionário
nome = str(input("\033[1;33mDigita teu nome ae: \033[m"))
sobrenome = str(input("\033[1;33mAgora o teu sobrenome kkkkkkkkkk: \033[m"))
print("\033[1;33mNem precisa do sobrenome pedi só pra encher o saco kkkkkk \033[m😂🤣")
sleep(1.5)

quer_casa = str(input("\033[1;33mTu quer compra uma casa?\033[m \033[36m(sim/não): \033[m "))
if quer_casa.lower() == "não":
    print("\033[1;31mE n t ã o    v a i    t o m a    n o    s e u    c u ,    t a    a q u i    p r a    q    e n t ã o    p r r  ? ? ? ? ? \033[m")
print("\033[1;33mPobre desse jeito kkkkk\033[m")
sleep(1.5)

valor_casa = float(input("\033[1;33mQual o valor desse barraco ae fi? \033[m"))
salario_mensal = float(input("\033[1;33mE quanto tu ganha por mês? \033[m"))

if salario_mensal >= 1000000:
    print("\033[1;33Tá com o pataco ein fi\nSai daqui e vai comprar essa casa a vista\033[m!!!!")
else:
    print("\033[1;31mTa quebrado irmao!! \033[m")

anos_para_pagar = int(input("\033[1;33mE em quantos anos quer quitar toda essa fita zé? \033[m"))

# Cálculos
total_meses = anos_para_pagar * 12
parcela_mensal = valor_casa / total_meses
limite_parcela = salario_mensal * 0.3  # 30% do salário

# Resultado
print("\033[1;37mCalculando.\033[m")
sleep(2)
print("\033[1;37mCalculando..\033[m")
sleep(2)
print("\033[1;37mCalculando...\033[m")
sleep(1.5)
print("\033[1;37mCalculando.\033[m")
sleep(1.5)
print("\033[1;37mCalculando..\033[m")
sleep(1)
print("\033[1;37mCalculando...\033[m")
sleep(1)
print("\033[1;37mCalculando.\033[m")
sleep(0.5)
print("\033[1;37mCalculando..\033[m")
sleep(0.5)
print("\033[1;37mCalculando...\033[m")
sleep(1.5)
print("\033[1;36;47mP R O N T O  ! ! !\033[m")
sleep(2)
if parcela_mensal <= limite_parcela:
    print(f"\033[1;33mSeguinte {nome}, oce quer comprar um barraco de\033[m \033[1;32mR${valor_casa:.2f} \033[m\033[1;33mganhando\033[m \033[1;32mR${salario_mensal:.2f}\033[m \033[1;33mpor mês.\033[m")
    print(f"\033[1;33mParcelando em {anos_para_pagar} anos ({total_meses} meses), a parcela fica\033[m \033[1;32mR${parcela_mensal:.2f}\033[m")
    print(f"\033[1;33mE como isso é menos que 30% do seu pataco, O seu emprestimo esta\033[m    \033[1;32mA  P  R  O  V  A  D  O\033[m    \033[1;33mfi, vai que é tua!\033[m")
else:
    print(f"\033[1;33mSeguinte {nome}, oce quer comprar um barraco de\033[m \033[1;32mR${valor_casa:.2f}\033[m \033[1;33mganhando\033[m \033[1;32mR${salario_mensal:.2f}\033[m \033[1;33mpor mês.\033[m")
    print(f"\033[1;33mMas a parcela de \033[1;32mR${parcela_mensal:.2f}\033[m \033[1;33mé maior que os 30% do seu salário\033[m \033[1;32m({limite_parcela:.2f}).\033[m")
    print("\033[1;33mInfelizmente o emprestimo foi\033[m     \033[1;31mN   E   G   A   D   O\033[m     \033[1;33m Tu vai ter que juntar mais uma grana aí.\033[m")
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW C a B O WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW