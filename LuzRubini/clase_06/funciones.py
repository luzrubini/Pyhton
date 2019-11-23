def saludar(nombre):
	print("Hola",nombre);

#saludar("Luz")

def multiplicar(numA, numB):
	return(numA*numB)

#print("El resultado de tu multiplicacion es: ",multiplicar(3,2))

#obtener instrucciones:
#Tiene que devolver las instrucciones para definir una funcion

def obtener_instrucciones ():
	return """

		Se utiliza la palabra clave def al comienzo.
		Luego se agrega el nombre de la función (en minusculas y las palabras separadas por guion).
		Se abre parentesis, que pueden recibir o no variables.
		Luego se utiliza dos puntos.
		El código a ejecutar dentro de la funcìón debe estar tabulado un espacio a la derecha. 
	"""

def imprimir_instrucciones():
	print("Instrucciones: \n", obtener_instrucciones())

#imprimir_instrucciones()

def saludar_por_cumpleanios(nombre, edad):
	print("Feliz cumple",nombre,"Ya tenes",edad,"años!!!!")

#saludar_por_cumpleanios("Luz","22")

def saludar_por_cumpleanios1(nombre = "Tincho", edad = 35):
	print("Feliz cumple",nombre,"Ya tenes",edad,"años!!!!")

#saludar_por_cumpleanios(edad = 43, nombre = "Carlitos")

#def funcion(*args, **kwargs) *args = multiples variables (tuplas)
#Ejemplo:
def sumar(*args): #tiene infinitos numeros. ----> Parametro posicional
	resultado = 0
	for n in args:
		resultado += n
	return resultado
print(sumar(10,12,25,23,26,28,29,63))

print("Si le paso una tupla:")
numeros = (10,12,25,23,26,28,29,63)
print(sumar(*numeros))

def saludar_por_cumpleanios(**kwargs): #----> diccionarios
	print("Feliz cumple",kwargs["nombre"],"Ya tenes",kwargs["edad"],"años!!!!")

datos = {"nombre" : "Carlitos" , "edad" : 43}
saludar_por_cumpleanios(**datos)