"""Examen Final Programación1"""

"""Ejercicio 1:
Un oficial de correos decide optimizar el trabajo de su oficina haciendo un programa que permita 
introducir el texto de un telegrama y corte todas las palabras de más de cinco letras dejando 
sólo las primeras cinco letras e indicando que una palabra fue cortada con el agregado de una arroba (@). 
El programa deberá mostrar el texto resultante.
Por ejemplo, al texto "Llego mañana alrededor del mediodía" se transcribe como 
"Llego mañan@ alred@ del medio@".
"""
telegrama1 = "Llego mañana alrededor del mediodía"
telegrama2= "Un oficial de correos decide optimizar el trabajo de su oficina haciendo un programa"


def cortar_telegrama(telegrama):
    tel=[]
    tel_split=telegrama.split()
    print(tel_split)
    for pal in tel_split:
        if len(pal)<=5:
            tel.append(pal)
        elif len(pal)>5:
            str=pal[:5]+"@"
            tel.append(str)
    mensaje= " ".join(tel)
    return mensaje

print(cortar_telegrama(telegrama1))

"""Ejercicio 2:
Hacer una función que dada una lista de palabras y un número entero k, 
retorne dos listas de palabras, una con las palabras de longitud menor o igual a k
y otra lista con las palabras de longitud mayor a k.
"""

lista1=["libro","bucle","lapicera","instrucción","exámen","programación"]

numero_k=5

def longitud_k(lista,num_k):
    lista_menor_igual_k=[]
    lista_mayor_k=[]
    print(lista)
    for palabra in lista:
        if len(palabra)<=num_k:
            lista_menor_igual_k.append(palabra)
        else:
            lista_mayor_k.append(palabra)
    return lista_menor_igual_k, lista_mayor_k

#print(longitud_k(lista1,numero_k))

"""Ejercicio 3:
Detectar y corregir los errores del siguiente programa que elimina y retorna un teléfono conociendo el 
nombre del usuario:

agenda = {'Juan':123456789, 'Pedro':987654321} 
def elimina(agenda, usuario): 
del listin[usuario]
return listin[usuario] 

print(elimina(listin, 'Pablo')) 

"""
agenda1 = {'Juan':123456789, 'Pedro':987654321} 

def elimina(agenda, usuario):
    mensaje=""
    if usuario in agenda: 
        del agenda[usuario]
        mensaje="usuario eliminado con éxito"
    else:
        mensaje="usuario inexistente"
    return mensaje,agenda 

#print(elimina(agenda1, 'Juan')) 



