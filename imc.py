def imc (tup):
	cont = 0
	for imc in tup:
		if imc > 30:
			cont += 1
	print ("Hay", cont, "Indices Mayores a 30")
if __name__ == '__main__':
	peso = float()
	talla = float()
	imc = float()
	print("ingrese su peso")
	peso = float(input())
	print("ingrese su talla")
	talla = float(input())
	imc = (talla*talla)
	imc = peso/imc
	print("su indice de masa corporal es",imc)
def imc (tup):
	cont = 0
	for imc in tup:
		if imc > 30:
			cont += 1
	print ("Hay", cont, "Indices Mayores a 30")