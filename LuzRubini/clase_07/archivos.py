print("Abro el archivo")

#archivo = open("texto.txt","r")
#archivo.close()


print("\nLeyendo archivo")
archivo = open("texto.txt","r")

#Leyendo caracteres del archivo
#print(archivo.read(1))
#print(archivo.read(6)) corre el puntero al final de lo que lee.

#Leyendo todo
#print(archivo.read())

#Leyendo por linea
#print(archivo.readline()) #corre el puntero al final de lo que lee.

#Volcando el arch a una lista.
#lineas = archivo.reanlines()
#print(lineas)



#Iterar directo el archivo

for linea in archivo:
	print(linea)
archivo.close()

print("\nEscritura archivo")
archivo = open("20191026.txt","w")

archivo.write("linea\n")

archivo.close()

#Biblioteca python: pickle.