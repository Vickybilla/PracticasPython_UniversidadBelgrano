"""escribir funciones que dada una cadena de caracteres:
a) imprima los 2 primeros caracteres
b)imprimir los {ultimos 3 caracteres
c) imprima dicha cadea cada dos caracteres: ej "recta" deber{ia imprimir rca
d)Dicha cadena en sentido inverso
e) imprima la cadena en un sentido y en sentido inverso"""

def ejercicio618a(cadena):
    return cadena[:2]

def ejercicio618b(cadena):
    return cadena[-3::]


def ejercicio618c(cadena):
    return cadena[::2]

def ejercicio618d(cadena):
    return cadena[::-1]

def ejercicio618e(cadena):
    return cadena+cadena[::-1]  

    
cad= "Atencion Virtual, Asesoramiento"

"""Ejercicio 682   dada una cadena y un caracter:
a) inserte un caracter entre cada letra de la cadena
b) reemplace todos los espacios por un caracter x
c) reemplace todos los dígitos por un caracter
d)inserte el caracter cada 3 dígitos en la cadena"""

caracter="."

def ejercicio682a (cadena,caracter):
    return caracter.join(cadena)

def ejercicio682b(cadena,caracter):
    cadena= cadena.replace(" ",caracter)
    return cadena

def ejercicio682c(cadena, caracter):
    for c in cadena:
        if c.isdigit():
            cadena= cadena.replace(c,caracter)
    return cadena

def ejercicio682d(cadena, caracter):
    cadena_pto=""
    cont=0
    for c in cadena:
        if cont!=0 and cont%3==0:
            cadena_pto=cadena_pto+caracter
        cadena_pto=cadena_pto+c
        cont=cont+1
    return cadena_pto


"""funcion que reciba un número y lo devuelva separado en miles"""

def ejercicio684(cadena,caracter):
    cadena_punto=""
    cont=1
    for c in cadena[::-1]:
        cadena_punto=c+cadena_punto
        if cont%3==0:
            cadena_punto=caracter+cadena_punto
        cont=cont+1
    return cadena_punto

"""Escribir una funcion que dada una cadena de caracteres devuelva.
a)La primer letra de cada palabra como sigla
b)la cadena con la primera letra en mayúsculas
c)las palabras que comiencen con la letra A"""

def ejercicio685a(cadena):
    cadena_split=cadena.split(" ")
    sigla=""
    for c in cadena_split:
        sigla+=c[0]
    return sigla


def ejercicio685b(cadena):
    cadena=cadena.title()
    return cadena

def ejercicio685c(cadena):
    cadena_split=cadena.split(" ")
    print(cadena_split)
    palabras_A=[]
    for c in cadena_split:
        if c[0]=="A"or c[0]=="a":
            palabras_A.append(c)
    return palabras_A

#print(ejercicio682a(cad,caracter))
#print(ejercicio682b(cad,caracter))
#print(ejercicio682c(cad,caracter))
#print(ejercicio682d(cad,caracter))
#print(ejercicio684(cad,caracter))
#print(ejercicio685a(cad))
#print(ejercicio685b(cad))
print(ejercicio685c(cad))
