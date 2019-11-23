
texto = input("Ingrese un mensaje: ")
texto.lower()
#Cantidad de caracteres
#Saber si en el texto se encuentra la e

print("\nLongitud del texto:", len(texto))
#El end="" evita el salto de linea
print("\nLa vocal más comun del español, 'e', ",end="")
if "e" in texto:
	print("está en el texto.")
else: 
	print("NO está en el texto.")