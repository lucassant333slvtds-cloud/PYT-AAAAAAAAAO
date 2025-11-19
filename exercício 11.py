L = float(input("Qual a largura da parede? "))
A = float(input("Qual a altura da parede? "))
Area = L * A
print ("A parede com a dimenção {} x {} tem a área de {}m².".format(L,A,Area))
tinta = Area / 2
print ("Com a area de {}m² você presisa de {:.0f} litros de tinta".format(Area,tinta))
