from abc import ABC, abstractmethod


class Enemigo(ABC):
	@abstractmethod
	def morir(self):
		pass

class Alien(Enemigo):
	def morir(self):
		print("auch")

class Jugador:
	def reventar(self, enemigo):
		print("El jugador revienta un enemigo")
		enemigo.morir()


heroe = Jugador()
invasor = Alien()
heroe.reventar(invasor)