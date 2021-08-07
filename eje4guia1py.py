"""Ejercicio 4:
Diseña un programa que, dado un número entero, determine si éste es el doble de un
número impar. (Ejemplo: 14 es el doble de 7, que es impar.)
"""
#agregar validación de  ingreso solo número para para que la mitad no tenga decimales y trate todo como número entero
x = int(input("Ingrese un número entero par "))
while x % 2 != 0:
    print (" el número ingresado no es un número par")
    x = int(input("Ingrese un número entero par "))
"""if (x //2)% 2 != 0 :
    print ("El número ingresado es el doble de un número impar.")
else: 
    print ("El número ingresado es el doble de un número par.")"""

#divido el número ingresado por 2 y 
# sobre eso valido si el resultado al dividirse por 2 da un 
# resultado distinto de 0, si es así es impar, e imprimo ambos valores para confirmar
if (x //2)% 2 != 0 :
    print (x, "es el doble de ", x//2, " que es impar")
else: 
    print (x, "es el doble de ", x//2, " que es par")