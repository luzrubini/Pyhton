def leer_global():
	print("Variable 'valor' en leer_global()",valor)

def esconder_global():
	valor = -2
	print("Variable 'valor' en esconder_global()",valor)
def cambiar_global():
	global valor
	valor = -5
	print("Variable 'valor' en cambiar_global()",valor)

valor = 10
#print("A nivel global vale: ",valor)
leer_global()
print("Volviendo a lvl global despues de leer_global()", valor)
esconder_global()
print("Volviendo a lvl global despues de esconder_global()", valor)
cambiar_global()
print("Volviendo a lvl global despues de cambiar_global()", valor)