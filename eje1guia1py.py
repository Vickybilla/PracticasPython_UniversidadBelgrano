"""Ejercicio 1:
Diseña un programa que lea la edad de dos personas y diga quién es más joven, la
primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, 
hazlo saber con un mensaje adecuado"""

juan = int(input("ingrese la edad de juan: "))
beto = int(input("ingrese la edad de beto: "))
if juan < beto:
    print("'juan' es menor")
elif juan == beto:
    print ("'juan' tiene la misma edad de 'Beto'")
else:
    print("'beto' es menor")