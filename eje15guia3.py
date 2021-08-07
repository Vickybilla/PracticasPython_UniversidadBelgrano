"""Ejercicio 15:
Dos palabras son anagramas si tienen las mismas letras pero en otro orden. Por ejemplo, 
«torpes» y «postre» son anagramas, mientras que «aparta» y «raptar» no lo son, ya que 
«raptar» tiene una r de más y una a de menos.
Escriba la función sonAnagramas(p1, p2) que indique si las palabras p1 y p2 son 
anagramas:
sonAnagramas('torpes', 'postre') ---> True
sonAnagramas('aparta', 'raptar') ---> False"""


def es_anagrama(cadena1, cadena2):
    return sorted(cadena1.lower()) == sorted(cadena2.lower())

primer_cadena=(input("Ingrese la primer palabra "))
segunda_cadena=(input("Ingrese la segunda palabra "))


print(es_anagrama(primer_cadena,segunda_cadena))