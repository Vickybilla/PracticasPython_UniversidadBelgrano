"""Ejercicio 7:
La ciudad de Babilonia tiene una alta congestión de vehículos circulando por sus calles. 
Las autoridades han decidido aplicar restricción vehicular para descongestionar la ciudad 
en base a las patentes de los vehículos.
La patente de un vehículo es un string de cuatro letras y dos dígitos, y la restricción 
depende sólo del penúltimo dígito. Por ejemplo, para la patente GEEA78, el dígito 7 es el 
utilizado para evaluar la restricción.
La restricción vehícular de los días hábiles de la semana se encuentra ingresada en el 
diccionario digitos, cuyas llaves son los días de la semanas, y cuyos valores son tuplas de 
cuatro enteros que representan los dígitos con restricción de ese día. 
• Implemente la función estaConRestriccion(digitos,dia, patente), que indique si el 
vehículo está o no con restricción.
• Implemente la función diasConRestriccion(digitos,patente), que retorne la lista de 
los días en que el vehículo no puede circular.
• Implemente la función diasSinRestriccion(digitos,patente), que retorne el conjunto 
de los días en que el vehículo sí puede circular.
digitos = {'lunes': (3, 4, 5, 6), 'martes': (7, 8, 9, 0),...,'miercoles': (1, 2, 3, 4), 'jueves': 
(5, 6, 7, 8), ... , 'viernes': (9, 0, 1, 2)}
estaConRestriccion(digitos, 'lunes', 'BBDT35') ---> True
diasConRestriccion(digitos, 'BBDT35') ---> ['lunes', 'miercoles']
diasSinRestriccion(digitos, 'BBDT35') ---> set(['jueves', 'martes', 'viernes']"""

digitos = {
        'lunes': (3, 4, 5, 6),
        'martes': (7, 8, 9, 0),
        'miercoles': (1, 2, 3, 4), 
        'jueves': (5, 6, 7, 8),
        'viernes': (9, 0, 1, 2)
        }

def estaConRestriccion(dic,dia,patente):
    restringido=dic.get(dia)
    digito_verificador=int(patente[-2])
    if digito_verificador in restringido:
        return True
    else:
        False

def diasConRestriccion(dic, patente):
    dias_restringidos=[]
    digito_verificador=int(patente[-2])
    for dia, num in dic.items():
        if digito_verificador in num:
            dias_restringidos.append(dia)
    return dias_restringidos

def diasSinRestriccion(dic, patente):
    dias_libres=[]
    digito_verificador=int(patente[-2])
    for dia, num in dic.items():
        if digito_verificador not in num:
            dias_libres.append(dia)
    return set(dias_libres)



#print(estaConRestriccion(digitos,"lunes","BBDT35"))

print(diasConRestriccion(digitos,"BBDT35"))

print(diasSinRestriccion(digitos, 'BBDT35'))