print("Battala del guerero")
salud = 10
trolls_derrotados = 0
ataque_de_troll = 3

while salud > 0:
	trolls_derrotados +=1
	salud -= ataque_de_troll
	print("Nuestro guerero venció a un troll ")
	print("Pero recibió",ataque_de_troll,"puntos de ataque")

print("================================")
print("El guerrero venció a ", trolls_derrotados, "trolls")
print("Pero... es un fiambre")