"""Ejercicio 16:
Las palabras panvocálicas son las que tienen las cinco vocales. Por ejemplo: centrifugado, 
bisabuelo, hipotenusa. Escriba la función esPanvocalica(palabra) que indique si una 
palabra es panvocálica o no:
esPanvocalica('educativo') ---> True
esPanvocalica('pedagogico') ---> False"""

def es_panvocalica (palabra):
    vocales="aeiou"
    auxvocales=""
    for c in palabra:
        if c in vocales:
            auxvocales= auxvocales+c
            print(auxvocales)
        sorted(vocales.lower()) == sorted(auxvocales.lower())
        print(auxvocales)
        return True
    else:
        return False


print(es_panvocalica("pedagogico"))