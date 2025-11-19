secsu = str(input('sexo [M/F]: ')).strip().upper()[0]
if secsu == 'M':
    print('Sexo masculino registrado com sucesso!')
elif secsu == 'F':
    print('Sexo feminino registrado com sucesso!')
else:
    Rept = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
    while Rept not in 'MF':
        Rept = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
    print('Sexo {} registrado com sucesso!'.format(Rept))
