"""Ejercicio 6:
Escribir un programa que permita ingresar tres números enteros y escribirlos en orden 
creciente"""

n1 = int(input("Ingrese  el primer número entero  "))
n2 = int(input("Ingrese  el segundo número entero  "))
n3 = int(input("Ingrese  el tercer número entero  "))

menor = min(n1,n2,n3)#obtiene el menor de la tupla
mayor = max(n1,n2, n3) #obtiene el mayor de la tupla
medio = (n1+n2+n3)-menor - mayor

print(" Los números ordenados de forma creciente son" ,menor,",", medio, ",", mayor)

#opcion 2
# #con if
