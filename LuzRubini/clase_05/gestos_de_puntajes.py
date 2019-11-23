#menu con itemms = 0 : salir, 1 : mostrar puntajes, 2 : agregar puntaje, 3 : eliminar puntaje, 4 : ordenar puntajes.
puntajes = []
respuesta = None 
while respuesta != "0":
	print("Menú de puntajes\n0-Salir\n1-Mostrar\n2-Agregar\n3-Eliminar\n4-Ordenar")
	respuesta = input("Ingresar opcion: ")
	if respuesta == "0":
		print("Hasta luego!!!!")
	elif respuesta == "1":
		print("Puntajes")
		for elemento in puntajes:
			print("-",elemento)
	elif respuesta == "2":
		nuevo_elemento = int(input("ingrese puntaje que desea agregar: "))
		puntajes.append(nuevo_elemento)
	elif respuesta == "3":
		borrar_elemento = int(input("ingrese puntaje a eliminar: "))
		if borrar_elemento in puntajes:
			puntajes.remove(borrar_elemento)
		else:
			print("El puntaje no astá")
	elif respuesta == "4":
		puntajes.sort(reverse=True)
	else:
		print("Respuesta incorrecta")
input("Enter para continuar")