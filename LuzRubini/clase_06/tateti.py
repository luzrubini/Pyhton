#1.a Tiene que mostrar un tablero de 9x9
# 1 | 2 | 3
# ----------
# 4 | 5 | 6
# ----------
# 7 | 8 | 9
#1.b Mostrar instrucciones
#2. Determinar quien va primero
#3. Crear y mostrar tablero vacio
#4. Mientras que nadie haya ganado y no haya empate:
#		Si es turno humano: 
#							Obtener movimiento humano.
#		Si es turno máquina:
#							Calcular el mov. de la máquina.
#		Actualizar movimiento
#		Mostrar tablero
#		Se cambia el turno
#5. Felicita a quien ganó o se declara empate.

# Mov de máquina preferibles 4,0,2,6,8,1,3,5,7
	# 1. Tratar de ganar
	# 2. Tratar de no perder

# Listado de funciones:
	# mostrar_instrucciones()
	# solicitar_numero(texto, minimo = 0, max = 9)
	# obtener_orden() tira rand para chequear si el humano tiene x u o
	# crear_tablero()
	# mostrar_tablero(tablero)
	# obtener_movimientos_posibles(tablero) retorna lugares vacios
	# obtener_ganador(tablero) tupla de tuplas
	# obtener_movimiento_humano(tablero)
	# obtener_movimiento_computadora(tablero, ficha_computadora, ficha_humano)
	# obtener_siguiente_turno(ficha)
	# felicitar_ganador()
	# main() -----> todo el programa.