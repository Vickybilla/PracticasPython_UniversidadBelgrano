"""Ejercicio 7:
Escribir un programa que permita ingresar el mes y el año y muestre la cantidad de días 
del mes. Por ejemplo, si el usuario ingresa mes 2 y año 2000, el programa debe responder 
que Febrero 2000 tiene 29 días. Si el usuario ingresa mes 3 y año 2005, el programa 
responderá que Marzo 2005 tiene 31 días.
"""

#se crea diccionario con clave valor de mes
meses={1:"Enero",
2:"Febrero",
3:"Marzo",
4:"Abril",
5:"Mayo",
6:"Junio",
7: "julio",
8:"agosto",
9:"septiembre",
10:"octubre",
11:"noviembre",
12:"diciembre"}


#Matemáticamente podemos saber si un año es bisiesto si este es múltiplo de 4. 
# Si además es múltiplo de 100 no será bisiesto (tener en cuenta que 100 es múltiplo de 4 y 
# por tanto cualquier número que sea múltiplo de 100 también es múltiplo de 4)
#  a no ser que sea múltiplo de 400, que sí será bisiesto.
def es_bisiesto(year) -> int:
    return not year % 4 and (year % 100 or not year % 400) 

def obtener_dias_del_mes(mes: int, year: int) -> int:
    # Abril, junio, septiembre y noviembre tienen 30
    if mes in [4, 6, 9, 11]:
        return 30
    # Febrero depende de si es o no bisiesto
    if mes == 2:
        if es_bisiesto(year):
            return 29
        else:
            return 28
    else:
        # En caso contrario, tiene 31 días
        return 31


mes = int(input("Ingrese un mes "))

while mes < 0 or mes >12:
    print (" el número ingresado no corresponde a un mes del año")
    mes=int(input("Ingrese número del mes  "))

year = int(input("ingrese un año  "))
    
#del diccionario de meses traigo el valor a traves de la clave mes
mes_print= meses.get(mes)
es_bisiesto(year) 
dias = obtener_dias_del_mes(mes, year)

print("El Mes de ",mes_print , "del año", year, "tiene" ,dias, "días")