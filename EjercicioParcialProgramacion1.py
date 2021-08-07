"""Ejercicio 3: Un usuario necesita que se facture el uso de un teléfono.
Los datos con que cuenta son: tarifa por segundo, cuántas comunicaciones se realizaron,
la duración de cada comunicación expresada en segundos.
Se pide que hagamos un programa para ayudar al usuario a determinar el costo de cada comunicación."""

tarifa_por_segundo= float(input("Ingresa la tarifa por segundo que cobra tu compañía telefónica  "))
cantidad_comunicaciones=int(input("Ingresa la cantidad de comunicaciones realizadas  "))
duracion_llamadas_en_segundos= int(input("Ingresa la duración de las llamadas realizadas  "))

print (" El costo total de las comunicaciones realizadas es de $",
(tarifa_por_segundo*duracion_llamadas_en_segundos)*cantidad_comunicaciones ,"pesos")