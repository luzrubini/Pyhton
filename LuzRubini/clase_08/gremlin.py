class Gremlin:
	total = 0

	def __init__(self, nombre, humor):
		print("Nació un nuevo gremlin")
		self.__nombre = nombre
		#__ indica que un atributo es privated
		self.__humor = humor
		self.__class__.total += 1

	@property
	def nombre(self):
		return self.__nombre

	@nombre.setter
	def nombre(self, nuevo_nombre):
		if(nuevo_nombre == ""):
			print("El nuevo nommbre no puede ser un string vacio")
		else:
			self.__nombre = nuevo_nombre
			print("¡Nombre modificado!")

	@classmethod #decorador
	def status(cls):
		print("Cantidad de Gremlins", cls.total)

	def hablar(self):
		print("Hola soy", self.__nombre, "y estoy" ,self.__humor, "\n")

	def __str__(self):
		res = "Objeto gremlin\n"
		res += "nombre: " + self.__nombre + "\n"

		return res

def main():
	gizmo = Gremlin("Gizmo","aburrido")
	grem2 = Gremlin("Lucas","feliz")


	gizmo.hablar()
	grem2.hablar()

	print(gizmo)
	print(grem2) #imprime la descripcion del objeto, a menos que se tenga un def de __str__ y se muestre la informacion del objeto
	print(grem2.nombre)

	print("Accediendo al atributo de clase")
	print(Gremlin.total)

	grem3 = Gremlin("Jin","triste")
	grem4 = Gremlin("Bort","enojado")

	print("Accediendo al atributo de clase")
	print(Gremlin.total)

	print(grem2._Gremlin__humor)

	print(grem2.nombre)
	grem2.nombre = "Franco"
	print(grem2.nombre)

if __name__ == '__main__':
	main()