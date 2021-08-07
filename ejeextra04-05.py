"""Escribir un programa que muestre todos los números entre 100 y 1000 que sean divisibles por 5 y por 6"""
n = 5
#rango hasta 1000
for n in range (100,1001):
    if n % 5 == 0 and n % 6 == 0:
        print (n, end = " ")
print ("\n\n último valor de n:  " , n)