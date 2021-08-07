"""Ejercicio 12:
Escribe un programa que lea dos cadenas y devuelva el prefijo común más largo de
ambas. Ejemplo: las cadenas "politécnico" y "polinización" tienen como prefijo común más
largo a la cadena "poli"."""


def encontrar_prefijo (pal1,pal2):
    prefijo =""
    for l1,l2 in zip(pal1,pal2):
        #print(l1,l2)
        if l1 == l2:
            prefijo=prefijo + l1
        else:
            break
    return prefijo    
                

palabra1 = input("Ingrese su palabra ")
palabra2 = input ("ingrese su palabra ")

prefijo_comun = encontrar_prefijo(palabra1,palabra2)

print("El prefijo de las palabras es ", prefijo_comun)