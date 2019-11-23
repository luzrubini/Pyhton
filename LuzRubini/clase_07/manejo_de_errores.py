def dividir():
	x = float(input("Ingresar num:"))
	y = float(input("Ingresar num:"))
	return (x/y)
try:
	#num = float(input("Ingresar num:"))
	resultado = dividir()
	#print(num*5)
except ValueError as e:
	print("Tiene que ingresar numeros")
	print(e)
except ZeroDivisionError as e:
	print("El segundo numero no puede ser cero")
	print(e)
except Exception as e:
	print("Hubo un error",e)
else: #se ejecutara si y solo si no hubo ningun error en el try
	print(resultado)

#finally -> si necesito abrir una conexion con una base de datos 
#se ejecuta independientemente de un exception.(Cierre de conexion)