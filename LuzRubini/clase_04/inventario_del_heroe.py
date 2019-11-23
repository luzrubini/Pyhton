#Tuplas 

inventario = (
	"espada", "armadura", "escudo", "pocion de vida")

if not inventario:
	print("Tenes las manos vacias...")
else:
	print("Tus items: ")

	for elemento in inventario:
		print("*",elemento.title())

input("Enter para continuar...")