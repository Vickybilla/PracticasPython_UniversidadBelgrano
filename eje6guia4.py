"""Ejercicio 6:
Diseña una función que reciba una lista de cadenas y devuelva el prefijo común más
largo. Por ejemplo, la cadena "pol" es el prefijo común más largo de esta lista:
[’poliedro’, ’policia’, ’polifona’, ’polinizar’, ’polaridad’, ’politica’]"""

#from eje12guia3 import*
lista=["poliedro", "policia", "polifona", "polinizar", "polaridad", "politica"]

def encontrar_prefijo (lista):
    prefijo =""
    ziplist=list(zip(*lista))
    print(ziplist)
    for l1 in ziplist:
        l2=set(l1)
        if len(l2) == 1:
            prefijo+=str(l2.pop())
        else:
            break
    return prefijo    

#palabra1 = input("Ingrese su palabra ")
#palabra2 = input ("ingrese su palabra ")

prefijo_comun = encontrar_prefijo(lista)

print("El prefijo de las palabras es ", prefijo_comun)