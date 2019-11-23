#De un random 1-3 nos va a decir tres cosas
import random
humor=random.randint(1,3)

print("Estoy sintiendo tu energia")
print("Vos estas...")
if humor == 1:
	print(" :)")
elif humor == 2:
	print(" :|")
else:
	print(" :(")

input("Presione ENTER para continuar")