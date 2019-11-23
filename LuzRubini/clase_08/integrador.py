Clase Gremlin

__nombre
__hambre (int)
__aburrimiento (int)
+humor (str) -> propiedad getter
El humor es getter, dentro de ese getter va a salir a partir del hambre y el aburrimiento. 
Vamos a calcular la infelicidad a partir de hambre y aburrimiento 
Si infelicidad < 5 = feliz
	<=5 infelicidad <=10 = ok
	<=11 infelicidad <=15 = frustrado
	infelicidad >15 = enojado


4 comportamientos:
-hablar()
muestra nombre y como se siente
-comer(comida = 4)
resta al hambre
-jugar(diversion = 4)
resta al aburrimiento
__pasar_tiempo()
Le suma uno al hambre y al aburrimiento si lo hacemos hablar, si le damos de comer sube el aburrimiento
si lo hacemos jugar, el hambre sube.

Menu:
escuchar
jugar
alimentar
salir