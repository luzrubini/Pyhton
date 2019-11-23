|||||||||||||||||||||||||||||WEB|||||||||||||||||||||||||||||||||

============================HTTPS================================ 
-Comunicacion cifrada (no encriptada)
-Con un contrato definido entre partes para saber como 
decodificar el mensaje
========================Servidores Web===========================
-Apache
-Nginx
-IIS(.NET solo funciona con IIS)
=================================================================
>>>>>>>>>>>>>>>>>>>>>>>>>Tipos de cloud<<<<<<<<<<<<<<<<<<<<<<<<<<

>IAAS (Infrastructure as a service): Hosting en gral.

>PAAS (Platform as a service)
-Heroku
-Google App Engine
-Elastic Bininstall

>BAAS (Backend as a service): Mobile en gral.
-login
-push notifications
-pequeña bd
-Google: firebase
-Amazon Mobile

>SAAS (Software as a service): Todo software que no tenga 
necesidad de instalar.
@Ejemplos:
-GMail
-Google Drive
-Dropbox
-Office 365
=================================================================
Amazon web services (AWS):
-foco puesto en los servicios

Google:
-Redes propias
-provee a AWS de hardware (mas allá de ser competencia)
-Menos servicios, pero muy enfocados a la interfaz gráfica 
sencilla (todo a menos de 3 clicks de distancia).

=================================================================
========================Herramientas=============================
Frameworks_completos(Vienen con herramientas -fullstack-)
	>Django
		-viene con un admin que permite hacer ABM de cada tabla 
		que tengo en mi BD.
		-buena documentación.
	>TurboGears
		-admin propio x2
	>Web2Py
		-admin propio x3

Micro_frameworks(Se debe instalar algunos plugins)
	>Flask 
		-armado de formularios
		-templates html
		-reemplazo de veriables
	>Bottle
	>CherryPy
=================================================================

>>>python3 manage.py runserver #levanta un servidor
#Si queremos cambiar el puerto, se hace luego del comando ----> 0.8000 (0 es un atajo para 0.0.0.0)
#serv. no de django but python

>>>python3 manage.py runserver 8002 #Servidor local

php -S localhost:9876 #Server en php

ORM (Object R Management)

Tabla ---------> Clase

#No tiene el dominio completo del sql
#Mapeo entre tablas y clases (no todas)
#No vemos las tablas intermedias
#Relacion de muchos a muchos
#El ORM de django no hace join de bd de manera automatica

#
