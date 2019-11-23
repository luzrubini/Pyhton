#importar bibliotecas y modulos de Python
import random

random.randint(1,20) #del 1-20
random.randrange(20) #hasta el <20 = a -> random.randrange(19)+1

dado1 = random.randint(1,6)
dado2 = random.randrange(6)+1
dado3 = random.randint(1,6)

suma_dados = dado1 + dado2 + dado3

print("Tus dados fueron:")
print("*",dado1)
print("*",dado2)
print("*",dado3)
print("Por un total de: ",suma_dados)

input("Presione ENTER para continuar")