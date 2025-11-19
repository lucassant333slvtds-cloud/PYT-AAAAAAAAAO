M = float(input("Distancia em metros "))
Km = M / 1000
Hm = M / 100
Dam = M / 10
Dm = M * 10
Cm = M * 100
Mm = M * 1000
print ("A medida de {}m corresponte a: \n{}km \n{}Hm \n{}Dam \n{:.0f}Dm \n{:.0f}Cm \n{:.0f}Mm".format(M,Km,Hm,Dam,Dm,Cm,Mm))