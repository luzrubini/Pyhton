#a partir de un texto ingresado, debe eliminar las vocales e imprimirlo por pantalla sin ellas

texto = input("Ingrese un texto: ")

VOCALES="aeiou"

texto_sin_vocales=""

#En python no existen las constantes

for letra in texto:
	if letra.lower() not in VOCALES:
		texto_sin_vocales += letra
		print(texto_sin_vocales)

print("\nEl texto sin vocales es: ",texto_sin_vocales)

