N = str(input("Qual a nacionalidade do comprador? "))
Nome = str(input("Qual o nome do comprador? "))
Prd = str(input("Qual o produto? "))
Prç = float(input("Qual o preço do produto? R$"))
D = float(input("Qual o desconto do produto? %"))
Ds = D / 100
Des = Prç * Ds
valor = Prç - Des
print (" Olá {}, pelo fato de você ser {} você receberá {:.0F}% de \ndesconto e na compra de um {}, com o valor \nde R${:.2f} ele sairá por apenas R${:.2f} \nTENHA UM ÓTIMO DIA \n(☞ﾟヮﾟ)☞".format(Nome,N,D,Prd,Prç,valor))
