"""Ejercicio 4: El usuario anterior está conforme con el programa que realizamos para que lo ayude a determinar el costo de sus llamadas.
Pero ahora necesita diferenciar entre llamadas cortas y llamadas largas porque el costo no es el mismo. 
Se considera llamada larga aquella que dura 30 segundos o más.
Deberemos agregar al programa la tarifa de la tarifa de la llamada larga. 
Se pide modificar el programa anterior para que tenga en cuenta la nueva información.
La llamada se deberá facturar con la tarifa que corresponda."""

tarifa_por_segundo=float(input("Ingresa la tarifa por segundo que cobra tu compañía telefónica "))
cantidad_comunicaciones=int(input("Ingresa la cantidad de comunicaciones realizadas  "))
duracion_llamadas_en_segundos= int(input("Ingresa la duración de las llamadas realizadas  "))

#si la duración de la llamada es mayor a 30 segundos la tarifa por segundo se reduce en un 20 porciento
if duracion_llamadas_en_segundos >30:
    tarifa_por_segundo =tarifa_por_segundo-(tarifa_por_segundo*0.2)



print ("El costo total de las comunicaciones realizadas es de $",
(tarifa_por_segundo*duracion_llamadas_en_segundos)*cantidad_comunicaciones ,"pesos")