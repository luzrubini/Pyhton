#Listas

inventario = ["espada", "armadura", "escudo", "pocion de vida"]

if not inventario:
	print("Tenes las manos vacias...")
else:
	print("Tus items: ")

	for elemento in inventario:
		print("*",elemento)
		#print("*",elemento.title()) ----> .title() solo para tuplas

respuesta = input("¿Querés agregar otro elemento?\n(Presiona 0 para no agregar nada): ")

while respuesta != "0":
	inventario.append(respuesta)
	respuesta = input("¿Querés agregar otro elemento?\n(Presiona 0 para no agregar nada): ")

inventario[0]="brújula"
print("Tus items: ")
for elemento in inventario:
	print("*",elemento)

input("Enter para continuar...")

#Modulo en Python TimeIt y lo itera hasta poder darte un promedio de tiempo de ejecucion.