#numero del 1-100, si el numero no lo adivina -> le dice si es mas alto o mas bajo
import random

numero = random.randint(1,100)
print("Hay 100 numeros, intenta adivinar cual salió...")
respuesta = int(input("A ver si tenes suerte"))
intentos = 0

while respuesta != numero:

	if respuesta>numero:
		print("Te fuiste amuy lejos, mas abajo,")
	else:
		print("Un poco mas arriba")

	respuesta = int(input("Oh well here we go again..."))
	intentos +=1
	
print("Felicidades! lo lograste en ",intentos,"intentos")
input("Presione ENTER para continuar")